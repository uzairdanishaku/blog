# Generated by Django 5.0 on 2023-12-14 11:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blogs", "0002_alter_category_options_blog"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="blog_body",
            field=models.TextField(default=1, max_length=2000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="blog",
            name="short_description",
            field=models.TextField(max_length=500),
        ),
    ]
