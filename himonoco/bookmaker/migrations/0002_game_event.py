# Generated by Django 3.0.6 on 2020-05-05 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookmaker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bookmaker.Event'),
            preserve_default=False,
        ),
    ]
