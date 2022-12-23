from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=50,null=True)
    email = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=50, null=True)
    
    
    def __str__(self) -> str:
        return self.name