from django.db import models

class Abonent(models.Model):
    Name=models.CharField(max_length=30)
    Surname=models.CharField(max_length=30)
    Secondname=models.CharField(max_length=30)
    Rank=models.CharField(max_length=30)
    Tel=models.CharField(max_length=30)
    Ip_tel=models.CharField(max_length=30)

    def __str__(self):
        return self.name
# Create your models here.
