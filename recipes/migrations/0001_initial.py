# Generated by Django 4.2.14 on 2024-08-02 11:29

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
                ("title", models.CharField(max_length=300)),
                ("slug", models.SlugField(max_length=200, unique=True)),
                ("description", models.CharField(max_length=500)),
                (
                    "instructions",
                    djrichtextfield.models.RichTextField(max_length=10000),
                ),
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
                    "recipe_types",
                    models.CharField(
                        choices=[
                            ("baking", "Baking"),
                            ("breakfast", "Breakfast"),
                            ("drinks", "Drinks"),
                            ("main meal", "Main Meal"),
                            ("sauces", "Sauces"),
                            ("sides", "Sides"),
                            ("snacks", "Snacks"),
                            ("spice-mix", "Spice Mix"),
                            ("misc", "Misc"),
                        ],
                        default="baking",
                        max_length=50,
                    ),
                ),
                (
                    "cooking_method",
                    models.CharField(
                        choices=[
                            ("air fryer", "Air Fryer"),
                            ("bbq", "BBQ"),
                            ("hob", "Hob"),
                            ("no cook", "No Cook"),
                            ("oven", "Oven"),
                            ("pressure cooker", "Pressure Cooker"),
                            ("slow cooker", "Slow Cooker"),
                            ("other", "Other"),
                        ],
                        default="air fryer",
                        max_length=50,
                    ),
                ),
                ("servings", models.CharField(max_length=100)),
                ("posted_date", models.DateTimeField(auto_now=True)),
                ("freezable", models.BooleanField(default=False)),
                (
                    "favourites",
                    models.ManyToManyField(
                        blank=True,
                        default=None,
                        related_name="favourite",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
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
