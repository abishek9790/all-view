from django.db import models
from django.urls import reverse
# Create your models here.
class school(models.Model):
    name=models.CharField(max_length=20)
    loc=models.CharField(max_length=50)
    owner=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})


class student(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    schoolname=models.ForeignKey(school, on_delete=models.CASCADE,related_name='students')
