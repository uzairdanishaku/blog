# Generated by Django 4.2.6 on 2023-12-31 11:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blogs", "0007_remove_blog_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
    ]