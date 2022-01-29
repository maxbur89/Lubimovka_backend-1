# Generated by Django 3.2.7 on 2021-09-29 22:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Имя автора')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Название спектакля')),
            ],
            options={
                'verbose_name': 'Спектакль',
                'verbose_name_plural': 'Спектакли',
            },
        ),
        migrations.CreateModel(
            name='Play',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Название пьесы')),
                ('is_draft', models.BooleanField(default=True, verbose_name='Черновик')),
            ],
            options={
                'verbose_name': 'Пьеса',
                'verbose_name_plural': 'Пьесы',
            },
        ),
        migrations.CreateModel(
            name='PerformanceReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('reviewer_name', models.CharField(max_length=100, verbose_name='Имя зрителя')),
                ('text', models.TextField(max_length=500, verbose_name='Текст отзыва')),
                ('url', models.URLField(blank=True, unique=True, verbose_name='Ссылка на отзыв')),
                ('pub_date', models.DateTimeField(blank=True, verbose_name='Дата публикации')),
                ('performance', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reviews', to='library.performance', verbose_name='Спектакль')),
            ],
            options={
                'verbose_name': 'Отзыв зрителя на спектакль',
                'verbose_name_plural': 'Отзывы зрителей на спектакль',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='PerformanceMediaReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('media_name', models.CharField(max_length=100, verbose_name='Название медиа ресурса')),
                ('text', models.TextField(max_length=500, verbose_name='Текст отзыва')),
                ('image', models.ImageField(upload_to='reviews/', verbose_name='Изображение')),
                ('url', models.URLField(blank=True, unique=True, verbose_name='Ссылка на отзыв')),
                ('pub_date', models.DateTimeField(blank=True, verbose_name='Дата публикации')),
                ('performance', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='media_reviews', to='library.performance', verbose_name='Спектакль')),
            ],
            options={
                'verbose_name': 'Медиа отзыв на спектакль',
                'verbose_name_plural': 'Медиа отзывы на спектакль',
                'ordering': ('-created',),
            },
        ),
    ]