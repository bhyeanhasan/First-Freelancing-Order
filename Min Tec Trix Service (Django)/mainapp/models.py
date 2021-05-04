from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=500)
    img = models.ImageField(upload_to='pics')
    post = models.TextField()

    def get_absolute_url(self):
        return f"/details/{self.id}/"


