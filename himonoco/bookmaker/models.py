from django.db import models

# Create your models here.


class Player(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=100)
    players = models.ManyToManyField(to=Player)

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=100)
    event = models.ForeignKey(to=Event, on_delete=models.CASCADE)
    win_point = models.IntegerField()
    winner = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, blank=True, related_name="winner")

    def __str__(self):
        return self.name


class Spectator(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def points(self, event: Event):
        expectations = Expectation.objects.filter(game__event=event, spectator=self)
        current_sum = sum([expectation.calc_point() for expectation in expectations])
        return current_sum


class Expectation(models.Model):
    spectator = models.ForeignKey(to=Spectator, on_delete=models.CASCADE)
    game = models.ForeignKey(to=Game, on_delete=models.CASCADE)
    expected_winner = models.ForeignKey(Player, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["spectator", "game"]

    def __str__(self):
        return f"{self.game.name} - {self.expected_winner.name}({self.spectator.name})"

    def calc_point(self):
        lose_point = 0
        if self.game.winner is not None:
            if self.expected_winner == self.game.winner:
                return self.game.win_point

        return lose_point
