# Generated by Django 3.0.6 on 2020-05-05 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookmaker', '0002_game_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='players',
        ),
        migrations.CreateModel(
            name='Expectation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expected_winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmaker.Player')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmaker.Game')),
                ('spectator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmaker.Spectator')),
            ],
        ),
    ]
