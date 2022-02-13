# Generated by Django 3.2.11 on 2022-02-07 17:43

from django.db import migrations
from django.core.exceptions import ObjectDoesNotExist


def delete_image_project_contents(apps, schema_editor):
    """Remove not supported content from projects."""
    ContentType = apps.get_model("contenttypes", "ContentType")
    ProjectContent = apps.get_model("articles", "ProjectContent")

    try:
        image_content_type = ContentType.objects.get_by_natural_key(app_label="content_pages", model="image")
    except ObjectDoesNotExist: # do nothing if there is no `Image` content_type in database.
        return

    image_project_contents = ProjectContent.objects.filter(content_type=image_content_type)
    image_project_contents.delete()


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0002_image_in_blog_reqired"),
    ]

    operations = [
        migrations.RunPython(
            delete_image_project_contents,
        ),
    ]