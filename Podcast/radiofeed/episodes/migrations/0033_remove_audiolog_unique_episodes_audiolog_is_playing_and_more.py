# Generated by Django 4.1.7 on 2023-03-06 20:15


from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("episodes", "0032_audiolog_unique_episodes_audiolog_is_playing"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="audiolog",
            name="unique_episodes_audiolog_is_playing",
        ),
        migrations.RemoveField(
            model_name="audiolog",
            name="is_playing",
        ),
    ]
