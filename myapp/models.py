from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    branch=models.CharField(max_length=40)
    profile_pic=models.ImageField(upload_to="pics",blank=True)

    def __str__(self):
        return self.name