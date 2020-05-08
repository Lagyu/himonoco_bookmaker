from django.http import HttpResponseRedirect, Http404, HttpResponseNotFound
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, RedirectView
from django.shortcuts import render

from .models import Event, Game, Player, Spectator, Expectation
import urllib.parse

# Create your views here.


class EventListView(ListView):
    template_name = "bookmaker/events.html"
    model = Event


class GamesListView(ListView):
    template_name = "bookmaker/games.html"
    model = Game

    def get_queryset(self):
        event = Event.objects.get(id=self.kwargs["event"])  # type: Event
        return Game.objects.filter(event=event).select_related("event").select_related("winner")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # ここsqliteだとdistinctが動作しない
        event = Event.objects.get(id=self.kwargs["event"])
        distinct_spectators = Spectator.objects.filter(expectation__game__event=event).distinct()
        ordered_distinct_spectators = sorted(distinct_spectators,
                                             key=lambda x: x.points(event=event),
                                             reverse=True)
        context['spectators'] = ordered_distinct_spectators
        context["event"] = event
        return context


class GameDetailView(DetailView):
    template_name = "bookmaker/game.html"
    model = Game

    def get_context_data(self, **kwargs):
        context = super(GameDetailView, self).get_context_data(**kwargs)
        context["spec_name"] = urllib.parse.unquote(self.request.COOKIES.get("spec_name", ""))
        return context


class CreateExpectationView(View):
    def post(self, request, *args, **kwargs):
        spectator_name = request.POST["spectator-name"]
        player_id = int(request.POST["player-id"])
        game_id = int(request.POST["game-id"])

        spectator_obj = Spectator.objects.get_or_create(name=spectator_name)[0]
        player_obj = Player.objects.get(id=player_id)
        game_obj = Game.objects.get(id=game_id)

        if game_obj.winner is not None:
            return HttpResponseNotFound("すでに投票が締め切られています。次は頑張りましょう。")

        if Expectation.objects.filter(spectator=spectator_obj, game=game_obj).count() == 0:
            Expectation.objects.create(
                spectator=spectator_obj,
                expected_winner=player_obj,
                game=game_obj
            )
        else:
            expectation = Expectation.objects.get(
                spectator=spectator_obj,
                game=game_obj
            )

            expectation.expected_winner = player_obj
            expectation.save()

        url = reverse("game_detail", kwargs={"event": game_obj.event.id, "pk": game_obj.id})
        response = HttpResponseRedirect(url)

        response.set_cookie("spec_name", urllib.parse.quote(spectator_name))

        return response
