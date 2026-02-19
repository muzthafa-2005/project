from django.db import models

# Create your models here.
class shirt(models.Model):
    brand=models.CharField(max_length=100)
    size=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    rating=models.TextField()


    def __str__(self):
        return f"{self.brand}"

    
