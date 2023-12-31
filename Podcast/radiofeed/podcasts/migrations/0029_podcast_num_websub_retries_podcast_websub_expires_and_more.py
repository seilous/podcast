# Generated by Django 4.2.1 on 2023-05-20 07:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("podcasts", "0028_alter_podcast_parser_error"),
    ]

    operations = [
        migrations.AddField(
            model_name="podcast",
            name="num_websub_retries",
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="podcast",
            name="websub_expires",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="podcast",
            name="websub_hub",
            field=models.URLField(blank=True, max_length=2086, null=True),
        ),
        migrations.AddField(
            model_name="podcast",
            name="websub_mode",
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name="podcast",
            name="websub_secret",
            field=models.UUIDField(blank=True, null=True),
        ),
    ]
