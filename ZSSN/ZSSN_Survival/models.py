from pyexpat import model
from django.db import models

# models 

infected = (
    ("Non-Infected","Non-Infected"),
    ("Infected","Infected"),
    )
gender = (
    ("Male","Male"),
    ("Female","Female"),
    ("Other","Other"),
    )
    
class Survivor(models.Model):
    # By default id will be created for this model
    name = models.CharField(max_length=100,null=False)
    age = models.IntegerField()
    gender = models.CharField(null=False,choices=gender,max_length=50)
    longitude = models.FloatField(null=False)
    latitude = models.FloatField(null=False)
    is_infected = models.CharField(null=False,max_length=50,choices=infected, default=0)

    def __str__(self):
        return self.name


