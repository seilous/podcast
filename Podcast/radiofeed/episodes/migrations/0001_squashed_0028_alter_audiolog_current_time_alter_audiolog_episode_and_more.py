# Generated by Django 4.0.6 on 2022-07-17 11:07


import django.contrib.postgres.indexes
import django.contrib.postgres.search
import django.db.migrations.operations.special
import django.db.models.deletion
import django.db.models.expressions
import django.utils.timezone
import model_utils.fields
from django.conf import settings
from django.db import migrations, models

# Functions from the following migrations need manual copying.
# Move them and any dependencies into this file, then update the
# RunPython operations to refer to the local versions:
# radiofeed.episodes.migrations.0020_audiolog_unique_episodes_audiolog_is_playing


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        (
            "podcasts",
            "0001_squashed_0150_remove_subscription_unique_podcasts_subscription_user_podcast_and_more",
        ),
        ("users", "0002_user_autoplay"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Episode",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("guid", models.TextField()),
                ("pub_date", models.DateTimeField()),
                ("link", models.URLField(blank=True, max_length=500, null=True)),
                ("title", models.TextField(blank=True)),
                ("description", models.TextField(blank=True)),
                ("keywords", models.TextField(blank=True)),
                ("media_url", models.URLField(max_length=500)),
                ("media_type", models.CharField(max_length=20)),
                ("length", models.IntegerField(blank=True, null=True)),
                ("duration", models.CharField(blank=True, max_length=12)),
                ("explicit", models.BooleanField(default=False)),
                (
                    "podcast",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="podcasts.podcast",
                    ),
                ),
            ],
        ),
        migrations.AddIndex(
            model_name="episode",
            index=models.Index(
                fields=["podcast"], name="episodes_ep_podcast_3361d9_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="episode",
            index=models.Index(fields=["guid"], name="episodes_ep_guid_b00554_idx"),
        ),
        migrations.AddIndex(
            model_name="episode",
            index=models.Index(
                fields=["-pub_date"], name="episodes_ep_pub_dat_205e36_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="episode",
            index=models.Index(
                fields=["pub_date"], name="episodes_ep_pub_dat_60d1c1_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="episode",
            index=models.Index(fields=["title"], name="episodes_ep_title_4a6059_idx"),
        ),
        migrations.AddIndex(
            model_name="episode",
            index=models.Index(fields=["-title"], name="episodes_ep_title_ce2893_idx"),
        ),
        migrations.AddConstraint(
            model_name="episode",
            constraint=models.UniqueConstraint(
                fields=("podcast", "guid"), name="unique_episode"
            ),
        ),
        migrations.CreateModel(
            name="Bookmark",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                (
                    "episode",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="episodes.episode",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddIndex(
            model_name="bookmark",
            index=models.Index(
                fields=["-created"], name="episodes_bo_created_d69e08_idx"
            ),
        ),
        migrations.AddConstraint(
            model_name="bookmark",
            constraint=models.UniqueConstraint(
                fields=("user", "episode"), name="uniq_bookmark"
            ),
        ),
        migrations.AlterField(
            model_name="episode",
            name="duration",
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.RemoveIndex(
            model_name="episode",
            name="episodes_ep_title_4a6059_idx",
        ),
        migrations.RemoveIndex(
            model_name="episode",
            name="episodes_ep_title_ce2893_idx",
        ),
        migrations.AddField(
            model_name="episode",
            name="search_vector",
            field=django.contrib.postgres.search.SearchVectorField(
                editable=False, null=True
            ),
        ),
        migrations.AddIndex(
            model_name="episode",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["search_vector"], name="episodes_ep_search__466ef4_gin"
            ),
        ),
        migrations.RunSQL(
            sql="\n            CREATE TRIGGER episode_update_search_trigger\n            BEFORE INSERT OR UPDATE OF title, keywords, search_vector\n            ON episodes_episode\n            FOR EACH ROW EXECUTE PROCEDURE\n            tsvector_update_trigger(\n              search_vector, 'pg_catalog.english', title, keywords);\n            UPDATE episodes_episode SET search_vector = NULL;\n            ",
            reverse_sql="\n            DROP TRIGGER IF EXISTS episode_update_search_trigger\n            ON episodes_episode;\n            ",
        ),
        migrations.AlterField(
            model_name="episode",
            name="media_type",
            field=models.CharField(max_length=60),
        ),
        migrations.CreateModel(
            name="History",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                ("updated", models.DateTimeField()),
                ("completed", models.DateTimeField()),
                ("current_time", models.IntegerField(default=0)),
                (
                    "episode",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="episodes.episode",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddIndex(
            model_name="history",
            index=models.Index(
                fields=["-updated"], name="episodes_hi_updated_29f4e9_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="history",
            index=models.Index(
                fields=["-completed"], name="episodes_hi_complet_ebe4aa_idx"
            ),
        ),
        migrations.AddConstraint(
            model_name="history",
            constraint=models.UniqueConstraint(
                fields=("user", "episode"), name="uniq_history"
            ),
        ),
        migrations.AlterField(
            model_name="history",
            name="completed",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.RemoveIndex(
            model_name="history",
            name="episodes_hi_complet_ebe4aa_idx",
        ),
        migrations.RemoveField(
            model_name="history",
            name="completed",
        ),
        migrations.RenameModel(
            old_name="History",
            new_name="AudioLog",
        ),
        migrations.RemoveConstraint(
            model_name="audiolog",
            name="uniq_history",
        ),
        migrations.RemoveIndex(
            model_name="audiolog",
            name="episodes_hi_updated_29f4e9_idx",
        ),
        migrations.AddIndex(
            model_name="audiolog",
            index=models.Index(
                fields=["-updated"], name="episodes_au_updated_eb4a9e_idx"
            ),
        ),
        migrations.AddConstraint(
            model_name="audiolog",
            constraint=models.UniqueConstraint(
                fields=("user", "episode"), name="uniq_audio_log"
            ),
        ),
        migrations.AddField(
            model_name="audiolog",
            name="completed",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name="QueueItem",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                ("position", models.IntegerField(default=0)),
                (
                    "episode",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="episodes.episode",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddIndex(
            model_name="queueitem",
            index=models.Index(
                fields=["position"], name="episodes_qu_positio_58d480_idx"
            ),
        ),
        migrations.AddConstraint(
            model_name="queueitem",
            constraint=models.UniqueConstraint(
                fields=("user", "episode"), name="uniq_queue_item"
            ),
        ),
        migrations.AddConstraint(
            model_name="queueitem",
            constraint=models.UniqueConstraint(
                fields=("user", "position"), name="uniq_queue_item_position"
            ),
        ),
        migrations.RemoveConstraint(
            model_name="queueitem",
            name="uniq_queue_item_position",
        ),
        migrations.RenameModel(
            old_name="Bookmark",
            new_name="Favorite",
        ),
        migrations.RemoveConstraint(
            model_name="favorite",
            name="uniq_bookmark",
        ),
        migrations.RemoveIndex(
            model_name="favorite",
            name="episodes_bo_created_d69e08_idx",
        ),
        migrations.AddIndex(
            model_name="favorite",
            index=models.Index(
                fields=["-created"], name="episodes_fa_created_edc79e_idx"
            ),
        ),
        migrations.AddConstraint(
            model_name="favorite",
            constraint=models.UniqueConstraint(
                fields=("user", "episode"), name="uniq_favorite"
            ),
        ),
        migrations.AlterField(
            model_name="episode",
            name="id",
            field=models.BigAutoField(
                editable=False, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="episode",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AddIndex(
            model_name="episode",
            index=models.Index(
                fields=["podcast", "pub_date"], name="episodes_ep_podcast_a7abe0_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="episode",
            index=models.Index(
                fields=["podcast", "-pub_date"], name="episodes_ep_podcast_b9a49e_idx"
            ),
        ),
        migrations.AlterField(
            model_name="audiolog",
            name="id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="episode",
            name="id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="favorite",
            name="id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="episode",
            name="media_url",
            field=models.URLField(max_length=1000),
        ),
        migrations.AlterField(
            model_name="episode",
            name="length",
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="queueitem",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="audiolog",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="episode",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="favorite",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="episode",
            name="link",
            field=models.URLField(blank=True, max_length=2083, null=True),
        ),
        migrations.AlterField(
            model_name="episode",
            name="media_url",
            field=models.URLField(max_length=2083),
        ),
        migrations.AddField(
            model_name="episode",
            name="cover_url",
            field=models.URLField(blank=True, max_length=2083, null=True),
        ),
        migrations.AddField(
            model_name="episode",
            name="episode_type",
            field=models.CharField(default="full", max_length=30),
        ),
        migrations.AddField(
            model_name="episode",
            name="episode",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="episode",
            name="season",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddIndex(
            model_name="episode",
            index=models.Index(
                fields=["-pub_date", "-id"], name="episodes_ep_pub_dat_9b17cd_idx"
            ),
        ),
        migrations.AddField(
            model_name="audiolog",
            name="autoplay",
            field=models.BooleanField(default=False),
        ),
        migrations.RemoveConstraint(
            model_name="audiolog",
            name="uniq_audio_log",
        ),
        migrations.RemoveConstraint(
            model_name="episode",
            name="unique_episode",
        ),
        migrations.RemoveConstraint(
            model_name="favorite",
            name="uniq_favorite",
        ),
        migrations.AddConstraint(
            model_name="audiolog",
            constraint=models.UniqueConstraint(
                fields=("user", "episode"), name="unique_episodes_audiolog"
            ),
        ),
        migrations.AddConstraint(
            model_name="episode",
            constraint=models.UniqueConstraint(
                fields=("podcast", "guid"), name="unique_episodes_episode"
            ),
        ),
        migrations.AddConstraint(
            model_name="favorite",
            constraint=models.UniqueConstraint(
                fields=("user", "episode"), name="unique_episodes_favorite"
            ),
        ),
        migrations.RemoveConstraint(
            model_name="queueitem",
            name="uniq_queue_item",
        ),
        migrations.AddConstraint(
            model_name="queueitem",
            constraint=models.UniqueConstraint(
                fields=("user", "episode"), name="unique_episodes_queueitem"
            ),
        ),
        migrations.AddField(
            model_name="audiolog",
            name="is_playing",
            field=models.BooleanField(default=False),
        ),
        migrations.AddConstraint(
            model_name="audiolog",
            constraint=models.UniqueConstraint(
                condition=models.Q(("is_playing", True)),
                fields=("user", "is_playing"),
                name="unique_episodes_audiolog_is_playing",
            ),
        ),
        migrations.RemoveField(
            model_name="audiolog",
            name="autoplay",
        ),
        migrations.RemoveConstraint(
            model_name="audiolog",
            name="unique_episodes_audiolog_is_playing",
        ),
        migrations.RemoveField(
            model_name="audiolog",
            name="is_playing",
        ),
        migrations.AddIndex(
            model_name="audiolog",
            index=models.Index(
                fields=["updated"], name="episodes_au_updated_033e45_idx"
            ),
        ),
        migrations.RemoveField(
            model_name="episode",
            name="link",
        ),
        migrations.RunSQL(
            sql="DROP TRIGGER IF EXISTS episode_update_search_trigger ON episodes_episode;CREATE TRIGGER episode_update_search_trigger BEFORE INSERT OR UPDATE OF title, search_vector ON episodes_episode FOR EACH ROW EXECUTE PROCEDURE tsvector_update_trigger(search_vector, 'pg_catalog.english', title);UPDATE episodes_episode SET search_vector = NULL;",
            reverse_sql="DROP TRIGGER IF EXISTS episode_update_search_trigger ON episodes_episode;",
        ),
        migrations.AddField(
            model_name="audiolog",
            name="is_playing",
            field=models.BooleanField(default=False),
        ),
        migrations.AddConstraint(
            model_name="audiolog",
            constraint=models.UniqueConstraint(
                condition=models.Q(
                    ("is_playing", True),
                    ("user", django.db.models.expressions.F("user")),
                ),
                fields=("user", "is_playing"),
                name="unique_episodes_audiolog_is_playing",
            ),
        ),
        migrations.RemoveConstraint(
            model_name="audiolog",
            name="unique_episodes_audiolog_is_playing",
        ),
        migrations.RemoveField(
            model_name="audiolog",
            name="is_playing",
        ),
        migrations.AddField(
            model_name="episode",
            name="link",
            field=models.URLField(blank=True, max_length=2083, null=True),
        ),
        migrations.RenameModel(
            old_name="Favorite",
            new_name="Bookmark",
        ),
        migrations.RemoveConstraint(
            model_name="bookmark",
            name="unique_episodes_favorite",
        ),
        migrations.RemoveIndex(
            model_name="bookmark",
            name="episodes_fa_created_edc79e_idx",
        ),
        migrations.AddIndex(
            model_name="bookmark",
            index=models.Index(
                fields=["-created"], name="episodes_bo_created_d69e08_idx"
            ),
        ),
        migrations.AddConstraint(
            model_name="bookmark",
            constraint=models.UniqueConstraint(
                fields=("user", "episode"), name="unique_episodes_bookmark"
            ),
        ),
        migrations.DeleteModel(
            name="QueueItem",
        ),
        migrations.RemoveConstraint(
            model_name="audiolog",
            name="unique_episodes_audiolog",
        ),
        migrations.RemoveConstraint(
            model_name="bookmark",
            name="unique_episodes_bookmark",
        ),
        migrations.RemoveConstraint(
            model_name="episode",
            name="unique_episodes_episode",
        ),
        migrations.AddConstraint(
            model_name="audiolog",
            constraint=models.UniqueConstraint(
                fields=("user", "episode"), name="unique_episodes_audiolog_user_episode"
            ),
        ),
        migrations.AddConstraint(
            model_name="bookmark",
            constraint=models.UniqueConstraint(
                fields=("user", "episode"), name="unique_episodes_bookmark_user_episode"
            ),
        ),
        migrations.AddConstraint(
            model_name="episode",
            constraint=models.UniqueConstraint(
                fields=("podcast", "guid"), name="unique_episodes_episode_podcast_guid"
            ),
        ),
        migrations.RemoveIndex(
            model_name="audiolog",
            name="episodes_au_updated_eb4a9e_idx",
        ),
        migrations.RemoveIndex(
            model_name="audiolog",
            name="episodes_au_updated_033e45_idx",
        ),
        migrations.RenameField(
            model_name="audiolog",
            old_name="updated",
            new_name="listened",
        ),
        migrations.AddIndex(
            model_name="audiolog",
            index=models.Index(
                fields=["-listened"], name="episodes_au_listene_7f0fdd_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="audiolog",
            index=models.Index(
                fields=["listened"], name="episodes_au_listene_e5a9d5_idx"
            ),
        ),
        migrations.RemoveField(
            model_name="audiolog",
            name="completed",
        ),
        migrations.AlterField(
            model_name="audiolog",
            name="current_time",
            field=models.IntegerField(
                default=0, verbose_name="Timestamp Mark (Seconds)"
            ),
        ),
        migrations.AlterField(
            model_name="audiolog",
            name="episode",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="episodes.episode",
                verbose_name="Episode",
            ),
        ),
        migrations.AlterField(
            model_name="audiolog",
            name="listened",
            field=models.DateTimeField(verbose_name="Last Listened At"),
        ),
        migrations.AlterField(
            model_name="audiolog",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="User",
            ),
        ),
        migrations.AlterField(
            model_name="bookmark",
            name="episode",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="episodes.episode",
                verbose_name="User",
            ),
        ),
        migrations.AlterField(
            model_name="bookmark",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="User",
            ),
        ),
        migrations.AlterField(
            model_name="episode",
            name="cover_url",
            field=models.URLField(
                blank=True, max_length=2083, null=True, verbose_name="Cover Image"
            ),
        ),
        migrations.AlterField(
            model_name="episode",
            name="description",
            field=models.TextField(blank=True, verbose_name="Episode Description"),
        ),
        migrations.AlterField(
            model_name="episode",
            name="duration",
            field=models.CharField(
                blank=True, max_length=30, verbose_name="Duration (Text)"
            ),
        ),
        migrations.AlterField(
            model_name="episode",
            name="episode",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Season Episode Number"
            ),
        ),
        migrations.AlterField(
            model_name="episode",
            name="episode_type",
            field=models.CharField(
                default="full", max_length=30, verbose_name="Episode Type"
            ),
        ),
        migrations.AlterField(
            model_name="episode",
            name="explicit",
            field=models.BooleanField(
                default=False, verbose_name="Contains Explicit or Adult Content"
            ),
        ),
        migrations.AlterField(
            model_name="episode",
            name="guid",
            field=models.TextField(verbose_name="RSS Feed GUID"),
        ),
        migrations.AlterField(
            model_name="episode",
            name="keywords",
            field=models.TextField(blank=True, verbose_name="Episode Keywords"),
        ),
        migrations.AlterField(
            model_name="episode",
            name="length",
            field=models.BigIntegerField(
                blank=True, null=True, verbose_name="Duration (Seconds)"
            ),
        ),
        migrations.AlterField(
            model_name="episode",
            name="link",
            field=models.URLField(
                blank=True,
                max_length=2083,
                null=True,
                verbose_name="Episode Website Page",
            ),
        ),
        migrations.AlterField(
            model_name="episode",
            name="media_type",
            field=models.CharField(max_length=60, verbose_name="Audio MIME Type"),
        ),
        migrations.AlterField(
            model_name="episode",
            name="media_url",
            field=models.URLField(max_length=2083, verbose_name="Audio URL Source"),
        ),
        migrations.AlterField(
            model_name="episode",
            name="podcast",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="podcasts.podcast",
                verbose_name="Podcast",
            ),
        ),
        migrations.AlterField(
            model_name="episode",
            name="pub_date",
            field=models.DateTimeField(verbose_name="Release Date"),
        ),
        migrations.AlterField(
            model_name="episode",
            name="search_vector",
            field=django.contrib.postgres.search.SearchVectorField(
                editable=False, null=True, verbose_name="PostgreSQL Search Vector"
            ),
        ),
        migrations.AlterField(
            model_name="episode",
            name="season",
            field=models.IntegerField(blank=True, null=True, verbose_name="Season"),
        ),
        migrations.AlterField(
            model_name="episode",
            name="title",
            field=models.TextField(blank=True, verbose_name="Episode Title"),
        ),
    ]
