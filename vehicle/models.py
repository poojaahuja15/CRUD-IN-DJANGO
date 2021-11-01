from django.db import models

class vehicle(models.Model):
    vehicletype = models.CharField(max_length = 100)
    modelname = models.CharField(max_length = 100)
    vehiclecolor = models.CharField(max_length = 100)
    enginetype = models.CharField(max_length = 100)
