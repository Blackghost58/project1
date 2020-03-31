from django.db import models

class Abonent(models.Model):
    Name=models.CharField(max_length=30)
    Surname=models.CharField(max_length=30)
    Secondname=models.CharField(max_length=30)
    Rank=models.CharField(max_length=30)
    Tel=models.IntegerField(max_length=8)
    Ip_tel=models.IntegerField(max_length=8)

    def __str__(self):
        return self.Name
# Create your models here.
