# Generated by Django 3.2.9 on 2021-12-05 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_data_add_missing_main_settings'),
        ('content_pages', '0004_preamble'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderedperson',
            name='block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordered_persons', to='content_pages.personsblock', verbose_name='Блок персон'),
        ),
        migrations.CreateModel(
            name='ContentPersonRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('extended_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_person_roles', to='content_pages.orderedperson', verbose_name='Персона')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_person_roles', to='core.role', verbose_name='Роль')),
            ],
            options={
                'verbose_name': 'Роль у персоны в блоке',
                'verbose_name_plural': 'Роли персон в блоках',
            },
        ),
        migrations.AddField(
            model_name='orderedperson',
            name='roles',
            field=models.ManyToManyField(related_name='ordered_persons', through='content_pages.ContentPersonRole', to='core.Role', verbose_name='Роли персоны'),
        ),
        migrations.AddConstraint(
            model_name='contentpersonrole',
            constraint=models.UniqueConstraint(fields=('extended_person', 'role'), name='unique_role_per_extended_person'),
        ),
        migrations.RenameModel(
            old_name='OrderedPerson',
            new_name='ExtendedPerson',
        ),
        migrations.AlterField(
            model_name='extendedperson',
            name='block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extended_persons', to='content_pages.personsblock', verbose_name='Блок персон'),
        ),
        migrations.AlterField(
            model_name='extendedperson',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extended_persons', to='core.person', verbose_name='Персона/человек'),
        ),
        migrations.AlterField(
            model_name='extendedperson',
            name='roles',
            field=models.ManyToManyField(related_name='extended_persons', through='content_pages.ContentPersonRole', to='core.Role', verbose_name='Роли персоны'),
        ),
        migrations.RenameField(
            model_name='extendedperson',
            old_name='item',
            new_name='person',
        ),
    ]
