# Generated by Django 4.1.6 on 2023-02-10 11:02


from django.db import migrations


def set_default_websub_mode(apps, schema_editor):
    Podcast = apps.get_model("podcasts", "Podcast")
    Podcast.objects.filter(
        websub_hub__isnull=False, websub_expires__isnull=False
    ).update(websub_mode="subscribe")


class Migration(migrations.Migration):
    dependencies = [
        ("podcasts", "0020_remove_podcast_websub_requested_podcast_websub_mode"),
    ]

    operations = [
        migrations.RunPython(
            set_default_websub_mode, reverse_code=migrations.RunPython.noop
        )
    ]
