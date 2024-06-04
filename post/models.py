from django.db import models

# Create your models here.
class addNews(models.Model):
    title = models.TextField(max_length=20)
    text = models.TextField(max_length=20)
    date = models.DateField()
    image = models.ImageField(upload_to='image/')