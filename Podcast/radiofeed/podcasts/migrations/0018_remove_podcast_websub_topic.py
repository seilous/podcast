# Generated by Django 4.1.6 on 2023-02-09 14:10


from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("podcasts", "0017_set_default_websub_verified"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="podcast",
            name="websub_topic",
        ),
    ]
