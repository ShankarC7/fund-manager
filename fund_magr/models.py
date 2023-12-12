from django.db import models

# Create your models here.
class Example(models.Model):
    name=models.CharField(max_length=50)
    expenses=models.IntegerField()
    savings=models.IntegerField()
    investment=models.IntegerField()
    income=models.IntegerField()

