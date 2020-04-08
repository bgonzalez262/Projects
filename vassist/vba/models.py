from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=200)
    website = models.CharField(max_length=200, blank=True, null=True)
    about = models.TextField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return self.last_name + "," + self.first_name
