# Generated by Django 3.2.11 on 2022-01-28 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('afisha', '0001_initial'), ('afisha', '0002_alter_event_options'), ('afisha', '0003_baseevent')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Название события')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Событие',
                'verbose_name_plural': 'События',
            },
        ),
        migrations.CreateModel(
            name='BaseEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Базовое событие',
                'verbose_name_plural': 'Базовые события',
                'ordering': ('-created',),
            },
        ),
    ]