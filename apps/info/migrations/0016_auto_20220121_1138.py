# Generated by Django 3.2.11 on 2022-01-21 08:38

import random

import django.db.models.deletion
from django.db import migrations, models


def distribute_volunteers_to_festivals(apps, schema_editor):
    Volunteer = apps.get_model("info", "Volunteer")
    Festival = apps.get_model("info", "Festival")

    festivals = list(Festival.objects.all())

    for obj in Volunteer.objects.all():
        obj.festival = random.choice(festivals)
        obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ("info", "0015_alter_festivalteam_person"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="volunteer",
            name="unique_volunteer",
        ),
        migrations.RemoveField(
            model_name="festival",
            name="volunteers",
        ),
        migrations.RemoveField(
            model_name="volunteer",
            name="year",
        ),
        migrations.AddField(
            model_name="volunteer",
            name="festival",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="volunteers",
                to="info.festival",
                verbose_name="Фестиваль",
            ),
            preserve_default=False,
        ),
        migrations.AddConstraint(
            model_name="volunteer",
            constraint=models.UniqueConstraint(fields=("person", "festival"), name="unique_volunteer"),
        ),
        migrations.RunPython(distribute_volunteers_to_festivals),
    ]
