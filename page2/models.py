from django.db import models

class PersonalInfo(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    birth=models.DateField()