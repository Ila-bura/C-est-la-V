from django.db import models

# Contact Form


class Contact(models.Model):
    """
    A model to display a contact form
    """
    fname = models.CharField(max_length=150)
    lname = models.CharField(max_length=150)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"New message from {self.fname} {self.lname}: {self.body}"
