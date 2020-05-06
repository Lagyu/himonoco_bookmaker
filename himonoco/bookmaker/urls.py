from django.urls import include, path
from .views import EventListView, GamesListView, GameDetailView, CreateExpectationView

urlpatterns = [
    path("", EventListView.as_view(), name="events"),
    path("<int:event>/", GamesListView.as_view(), name="games"),
    path("<int:event>/<slug:pk>/", GameDetailView.as_view(), name="game_detail"),
    path("<int:event>/<slug:pk>/post/", CreateExpectationView.as_view(), name="create_expectation")
]