# Generated by Django 5.1 on 2024-08-29 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0003_contact_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contact",
            name="user",
        ),
    ]
