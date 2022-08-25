from django.db import models
from autoslug import AutoSlugField
class Posts(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    date = models.DateField(auto_now=True)
    slug = AutoSlugField(populate_from = "title" , unique = True , null = True , default = None)

class feedback(models.Model):
    Name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    Email = models.EmailField(max_length = 200)
    message = models.CharField(max_length=200)

