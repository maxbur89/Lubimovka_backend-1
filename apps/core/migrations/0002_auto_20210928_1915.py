# Generated by Django 3.2.7 on 2021-09-28 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('middle_name', models.CharField(blank=True, max_length=50, verbose_name='Отчество')),
                ('city', models.CharField(blank=True, max_length=50, verbose_name='Город проживания')),
                ('email', models.EmailField(blank=True, max_length=200, unique=True, verbose_name='Электронная почта')),
                ('image', models.ImageField(upload_to='images/person_avatars', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Человек',
                'verbose_name_plural': 'Люди',
                'ordering': ('last_name',),
            },
        ),
        migrations.AddConstraint(
            model_name='person',
            constraint=models.UniqueConstraint(fields=('first_name', 'last_name', 'middle_name', 'email'), name='unique_person'),
        ),
    ]