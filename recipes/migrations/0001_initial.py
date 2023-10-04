# Generated by Django 3.2.21 on 2023-10-02 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import djrichtextfield.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Recipe",
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
                ("title", models.CharField(max_length=350)),
                ("description", models.CharField(max_length=500)),
                ("method", djrichtextfield.models.RichTextField(max_length=10000)),
                ("ingredients", djrichtextfield.models.RichTextField(max_length=10000)),
                (
                    "image",
                    django_resized.forms.ResizedImageField(
                        crop=None,
                        force_format="WEBP",
                        keep_meta=True,
                        quality=75,
                        scale=None,
                        size=[400, None],
                        upload_to="recipes/",
                    ),
                ),
                ("image_alt", models.CharField(max_length=100)),
                (
                    "dish_type",
                    models.CharField(
                        choices=[
                            ("mains", "Mains"),
                            ("snacks", "Snacks"),
                            ("desserts", "Desserts"),
                        ],
                        default="mains",
                        max_length=50,
                    ),
                ),
                (
                    "prep_time",
                    models.CharField(
                        choices=[
                            ("10 minutes", "10 Minutes"),
                            ("15 minutes", "15 Minutes"),
                            ("20 minutes", "20 Minutes"),
                            ("25 minutes", "25 Minutes"),
                            ("30 minutes", "30 Minutes"),
                            ("35 minutes", "35 Minutes"),
                            ("40 minutes", "40 Minutes"),
                            ("45 minutes", "45 Minutes"),
                            ("50 minutes", "50 Minutes"),
                            ("55 minutes", "55 Minutes"),
                            ("1 hour", "1 Hour"),
                            ("1+ hour", "1+ Hour"),
                        ],
                        default="10 minutes",
                        max_length=50,
                    ),
                ),
                ("posted_date", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="recipe_owner",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-posted_date"],
            },
        ),
    ]
