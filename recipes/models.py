from django.db import models
from django.contrib.auth.models import User

from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField

# Choice Fields
DISH_TYPES = (("main", "Main"),
              ("snack", "Snack"), ("dessert", "Dessert"))

PREP_TIME = (("10 minutes", "10 Minutes"),
             ("15 minutes", "15 Minutes"), ("20 minutes", "20 Minutes"),
             ("25 minutes", "25 Minutes"), ("30 minutes", "30 Minutes"),
             ("35 minutes", "35 Minutes"), ("40 minutes", "40 Minutes"),
             ("45 minutes", "45 Minutes"), ("50 minutes", "50 Minutes"),
             ("55 minutes", "55 Minutes"), ("1 hour", "1 Hour"),
             ("1+ hour", "1+ Hour"))


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
        max_length=50, choices=PREP_TIME, default="10 minutes"
    )
    posted_date = models.DateTimeField(auto_now=True)

    """
    To be able to retrieve most recent recipes
    """
    class Meta:
        ordering = ["-posted_date"]

    def __str__(self):
        return str(self.title)
