# Generated by Django 5.1 on 2024-09-02 14:32

import files.models
import files.storage_backends
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("files", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Upload",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
                (
                    "file",
                    models.FileField(
                        storage=files.storage_backends.PublicMediaStorage(),
                        upload_to="",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UploadPrivate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
                (
                    "file",
                    models.FileField(
                        storage=files.storage_backends.PrivateMediaStorage(),
                        upload_to="",
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="userfile",
            name="file",
            field=models.FileField(
                storage=files.storage_backends.PublicMediaStorage(),
                upload_to=files.models.user_directory_path,
            ),
        ),
    ]
