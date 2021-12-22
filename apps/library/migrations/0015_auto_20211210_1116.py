# Generated by Django 3.2.9 on 2021-12-10 11:16

import apps.library.utilities
import django.core.validators
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0014_add_short_list_program'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participationapplicationfestival',
            name='file',
            field=models.FileField(help_text="Файл в одно из форматов ('doc', 'docx', 'txt', 'odt', 'pdf')", upload_to=apps.library.utilities.generate_class_name_path, validators=[django.core.validators.FileExtensionValidator(('doc', 'docx', 'txt', 'odt', 'pdf'))], verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='participationapplicationfestival',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='Номер телефона указывается в формате +7', max_length=128, region=None),
        ),
    ]