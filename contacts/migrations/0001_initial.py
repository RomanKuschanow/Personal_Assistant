
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                (
                    "first_name",
                    models.CharField(max_length=50, verbose_name="First Name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=50, verbose_name="Last Name"),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="Email Address"
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(max_length=15, verbose_name="Phone Number"),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Address"
                    ),
                ),
                (
                    "birthday",
                    models.DateField(blank=True, null=True, verbose_name="Birthday"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
            ],
            options={
                "verbose_name": "Contact",
                "verbose_name_plural": "Contacts",
            },
        ),
    ]
