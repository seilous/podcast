# Generated by Django 4.1.4 on 2022-12-15 07:31


from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("podcasts", "0011_remove_podcast_http_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="podcast",
            name="parse_result",
        ),
    ]
