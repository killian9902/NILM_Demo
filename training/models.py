from django.db import models


class Appliance(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class MeterReading(models.Model):
    appliance = models.ForeignKey(Appliance, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    Wh = models.FloatField()

    def __str__(self):
        return f'{self.appliance.name} - {self.datetime}: {self.Wh}Wh'