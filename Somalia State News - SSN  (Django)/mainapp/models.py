from django.db import models
from django.utils import timezone

# Create your models here.
class DP(models.Model):
    name = models.CharField(max_length=500)
    img = models.ImageField(upload_to='pics')
    post = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    job = models.BooleanField(default=False)
    breaking_news = models.BooleanField(default=False)
    editorial = models.BooleanField(default=False)

    def get_absolute_url(self):
        return f"/details/{self.id}/"


