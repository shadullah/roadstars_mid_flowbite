from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    borrowed_cars = models.ManyToManyField('cars.Cars', blank=True)

    def __str__(self):
        return self.user.username