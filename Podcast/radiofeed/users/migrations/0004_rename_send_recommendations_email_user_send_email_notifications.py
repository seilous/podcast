# Generated by Django 4.0.1 on 2022-01-05 10:47


from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_remove_user_autoplay"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="send_recommendations_email",
            new_name="send_email_notifications",
        ),
    ]
