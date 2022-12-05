# Generated by Django 4.1.3 on 2022-12-03 06:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("social", "0005_post_dislikes_post_like"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="dislikes",
            field=models.ManyToManyField(
                blank=True, related_name="comment_dislikes", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="like",
            field=models.ManyToManyField(
                blank=True, related_name="comment_likes", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]