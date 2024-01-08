from django.db import models
from categories.models import Brand
from django.contrib.auth.models import User

# Create your models here.
class Cars(models.Model):
    car= models.CharField(max_length=30)
    price = models.IntegerField()
    quantity = models.IntegerField()
    brand = models.ManyToManyField(Brand)
    image = models.ImageField(upload_to='cars/media/uploads/', blank=True, null = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.car


class Comment(models.Model):
    cars = models.ForeignKey(Cars, on_delete = models.CASCADE, related_name='comments')
    name = models.CharField(max_length = 30)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name