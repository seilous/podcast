# Generated by Django 4.1.7 on 2023-03-02 15:54


from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("podcasts", "0023_remove_podcast_websub_content"),
    ]

    operations = [
        migrations.AddField(
            model_name="podcast",
            name="num_websub_retries",
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
