# Generated by Django 3.1.3 on 2020-11-17 15:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myblog', '0007_auto_20201020_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='unlikes',
            field=models.ManyToManyField(related_name='blog_posts_unlike', to=settings.AUTH_USER_MODEL),
        ),
    ]
