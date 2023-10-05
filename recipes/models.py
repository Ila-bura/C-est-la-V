from django.db import models
from django.contrib.auth.models import User

from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField

# Choice Fields
DISH_TYPES = (("Main", "Main"), ("Snack", "Snack"),
              ("Dessert", "Dessert"))

PREP_TIME = (
    ("10 minutes", "10 min"),
    ("15 minutes", "15 min"),
    ("20 minutes", "20 min"),
    ("25 minutes", "25 min"),
    ("30 minutes", "30 min"),
    ("35 minutes", "35 min"),
    ("40 minutes", "40 min"),
    ("45 minutes", "45 min"),
    ("50 minutes", "50 min"),
    ("55 minutes", "55 min"),
    ("1 hour", "1h"),
    ("1+ hour", "more than 1h"),
)


class Recipe(models.Model):
    """
    A model to create and manage recipes
    Only recipe's creators can edit or delete their own recipes
    """

    user = models.ForeignKey(
        User, related_name="recipe_owner", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=350, null=False, blank=False)
    description = models.CharField(max_length=500, null=False, blank=False)
    method = RichTextField(max_length=10000, null=False, blank=False)
    ingredients = RichTextField(max_length=10000, null=False, blank=False)
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="recipes/",
        force_format="WEBP",
        blank=False,
        null=False,
    )
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    dish_type = models.CharField(
        max_length=50, choices=DISH_TYPES, default="main")
    prep_time = models.CharField(
        max_length=50, choices=PREP_TIME, default="10 minutes")
    posted_date = models.DateTimeField(auto_now=True)

    """
    To be able to retrieve most recent recipes
    """

    class Meta:
        ordering = ["-posted_date"]

    def __str__(self):
        return str(self.title)
