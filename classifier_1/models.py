from django.db import models

# Create your models here.
class ClassifierModel(models.Model):
    article = models.CharField(max_length=200)


    def __str__(self):
        return self.name