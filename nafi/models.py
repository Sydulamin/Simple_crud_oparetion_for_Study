from django.db import models


# Create your models here.
class Human(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    )

    name = models.CharField(max_length=25, unique=True)
    email = models.EmailField(max_length=25, null=True, blank=True)
    age = models.PositiveIntegerField(default=50)
    gender = models.CharField(choices=GENDER, max_length=7, null=True, blank=True, default='Male')
    image = models.ImageField(upload_to='images/', default='def.jpg', null=True, blank=True)
    address = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
