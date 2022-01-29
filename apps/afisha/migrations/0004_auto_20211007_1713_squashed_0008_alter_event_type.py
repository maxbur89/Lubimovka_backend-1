# Generated by Django 3.2.11 on 2022-01-28 19:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    replaces = [('afisha', '0004_auto_20211007_1713'), ('afisha', '0005_alter_event_url'), ('afisha', '0006_auto_20211127_0741'), ('afisha', '0007_alter_event_options'), ('afisha', '0008_alter_event_type')]

    dependencies = [
        ('afisha', '0001_initial_squashed_0003_baseevent'),
        ('library', '0001_squashed_0002_auto_20211004_1737'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BaseEvent',
            new_name='CommonEvent',
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('-created',), 'verbose_name': 'Событие', 'verbose_name_plural': 'События'},
        ),
        migrations.RemoveField(
            model_name='event',
            name='name',
        ),
        migrations.AddField(
            model_name='event',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата и время'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='paid',
            field=models.BooleanField(default=False, verbose_name='Платное'),
        ),
        migrations.AddField(
            model_name='event',
            name='place',
            field=models.CharField(default='Место', max_length=200, verbose_name='Место'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='pinned_on_main',
            field=models.BooleanField(default=False, verbose_name='Закрепить на главной'),
        ),
        migrations.AddField(
            model_name='event',
            name='common_event',
            field=models.ForeignKey(help_text='Создайте спектакль, читку или мастер-класс чтобы получить возможность создать соответствующее событие', on_delete=django.db.models.deletion.CASCADE, related_name='body', to='afisha.commonevent', verbose_name='Событие'),
        ),
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.CharField(choices=[('PERFORMANCE', 'Спектакль'), ('MASTERCLASS', 'Мастер-класс'), ('READING', 'Читка')], max_length=50, verbose_name='Тип события'),
        ),
        migrations.AddField(
            model_name='event',
            name='url',
            field=models.URLField(verbose_name='Ссылка'),
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('-date_time',), 'verbose_name': 'Событие', 'verbose_name_plural': 'События'},
        ),
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.CharField(blank=True, choices=[('PERFORMANCE', 'Спектакль'), ('MASTERCLASS', 'Мастер-класс'), ('READING', 'Читка')], max_length=50, verbose_name='Тип события'),
        ),
    ]
