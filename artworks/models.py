from django.db import models
from users.models import CustomUser

# Create your models here.
class Artwork(models.Model):
    title = models.CharField('title', blank=False, max_length=120)
    description = models.CharField('description', blank="True", max_length=120)
    image_url = models.CharField('Image URL', blank="True", max_length=120)
    date_created = models.DateTimeField(null=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)