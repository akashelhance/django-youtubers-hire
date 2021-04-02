from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django_resized import ResizedImageField

# Create your models here.
class Upload(models.Model):
    
    height=models.PositiveIntegerField(default=100, validators=[MinValueValidator(1), MaxValueValidator(1000)])
    width= models.PositiveIntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(1000)])
    img = models.ImageField(upload_to='media/resize/')
    post_image = ResizedImageField(size=[200,200], upload_to='media/resize/')
   
