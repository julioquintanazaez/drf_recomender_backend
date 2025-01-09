from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db import models

class User(models.Model):
    ROLE_CHOICES = [
        ('profesor', 'Profesor'),
        ('estudiante', 'Estudiante'),
        ('cliente', 'Cliente'),
    ]
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.name

class QualityData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    metric = models.CharField(max_length=100)
    value = models.FloatField()
    date_recorded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.metric}: {self.value} (User: {self.user.username})"

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

