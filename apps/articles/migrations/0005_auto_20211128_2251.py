# Generated by Django 3.2.9 on 2021-11-28 22:51

import apps.content_pages.utilities
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_data_initial_roles'),
        ('articles', '0004_auto_20211103_0037'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogitem',
            options={'ordering': ('-pub_date',), 'verbose_name': 'Запись блога', 'verbose_name_plural': 'Блог'},
        ),
        migrations.AddField(
            model_name='blogitem',
            name='is_draft',
            field=models.BooleanField(default=True, help_text='Поставьте отметку если это черновик', verbose_name='Черновик'),
        ),
        migrations.AddField(
            model_name='blogitem',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации'),
        ),
        migrations.AddField(
            model_name='newsitem',
            name='is_draft',
            field=models.BooleanField(default=True, help_text='Поставьте отметку если это черновик', verbose_name='Черновик'),
        ),
        migrations.AddField(
            model_name='project',
            name='is_draft',
            field=models.BooleanField(default=True, help_text='Поставьте отметку если это черновик', verbose_name='Черновик'),
        ),
        migrations.AddField(
            model_name='project',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='blogitem',
            name='description',
            field=models.TextField(max_length=500, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='blogitem',
            name='image',
            field=models.ImageField(blank=True, upload_to=apps.content_pages.utilities.path_by_app_label_and_class_name, verbose_name='Заглавная картинка'),
        ),
        migrations.AlterField(
            model_name='blogitem',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='description',
            field=models.TextField(max_length=500, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to=apps.content_pages.utilities.path_by_app_label_and_class_name, verbose_name='Заглавная картинка'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(max_length=500, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='images/articles/projects/', verbose_name='Заглавная картинка'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Заголовок'),
        ),
        migrations.CreateModel(
            name='BlogPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_persons', to='articles.blogitem', verbose_name='Блог')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='blog_persons', to='core.person', verbose_name='Соавтор блога')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='blog_persons', to='core.role', verbose_name='Роль в соавторстве')),
            ],
            options={
                'verbose_name': 'Соавтор блога',
                'verbose_name_plural': 'Соавторы блогов',
                'ordering': ('role',),
            },
        ),
        migrations.AddField(
            model_name='blogitem',
            name='roles',
            field=models.ManyToManyField(related_name='blogs', through='articles.BlogPerson', to='core.Role', verbose_name='Роли'),
        ),
        migrations.AddConstraint(
            model_name='blogperson',
            constraint=models.UniqueConstraint(fields=('person', 'blog', 'role'), name='unique_person_role_per_blog'),
        ),
    ]