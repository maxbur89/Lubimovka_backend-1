# Generated by Django 3.2.9 on 2021-11-10 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_auto_20211017_1522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='volunteer',
            old_name='review',
            new_name='review_text',
        ),
        migrations.AddField(
            model_name='volunteer',
            name='review_title',
            field=models.CharField(blank=True, max_length=50, verbose_name='Заголовок отзыва'),
        ),
    ]