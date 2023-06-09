from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=155)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    message = models.TextField(max_length=1200)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

