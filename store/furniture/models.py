from django.db import models

# Create your models here.

class Owner(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)

class Furniture(models.Model):
    KIND_MATERIAL = (
        ('P','PDC'),
        ('M','MDC'),
        ('W','Wooden'),
    )
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveIntegerField()
    image_url = models.URLField()
    material = models.CharField(max_length=1, choices=KIND_MATERIAL)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.model}, make {self.make}, id{self.pk}"


