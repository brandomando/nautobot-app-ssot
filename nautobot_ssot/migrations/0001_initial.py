# Generated by Django 3.1.12 on 2021-06-28 17:06

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("extras", "0005_configcontext_device_types"),
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sync",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("source", models.CharField(max_length=64)),
                ("target", models.CharField(max_length=64)),
                ("start_time", models.DateTimeField(null=True)),
                ("dry_run", models.BooleanField(default=False)),
                ("diff", models.JSONField()),
                (
                    "job_result",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to="extras.jobresult"
                    ),
                ),
            ],
            options={
                "ordering": ["start_time"],
            },
        ),
        migrations.CreateModel(
            name="SyncLogEntry",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("action", models.CharField(max_length=32)),
                ("status", models.CharField(max_length=32)),
                ("diff", models.JSONField(blank=True, null=True)),
                ("synced_object_id", models.UUIDField(blank=True, null=True)),
                ("object_repr", models.CharField(blank=True, default="", editable=False, max_length=200)),
                ("message", models.CharField(blank=True, max_length=511)),
                (
                    "sync",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="logs",
                        related_query_name="log",
                        to="nautobot_ssot.sync",
                    ),
                ),
                (
                    "synced_object_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="contenttypes.contenttype",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "sync log entries",
                "ordering": ["sync", "timestamp"],
            },
        ),
    ]
