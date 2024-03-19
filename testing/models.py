from django.db import models

class Feature(models.Model):
    feature1 = models.FloatField()
    feature2 = models.FloatField()
    feature3 = models.FloatField()
    feature4 = models.FloatField()
    feature5 = models.FloatField()
    feature6 = models.FloatField()
    feature7 = models.FloatField()
    feature8 = models.FloatField()
    feature9 = models.FloatField()
    feature10 = models.FloatField()
    feature11 = models.FloatField()
    feature12 = models.FloatField()
    feature13 = models.FloatField()
    feature14 = models.FloatField()
    feature15 = models.FloatField()
    feature16 = models.FloatField()
    feature17 = models.FloatField()
    feature18 = models.FloatField()
    feature19 = models.FloatField()
    feature20 = models.FloatField()
    feature21 = models.FloatField()
    feature22 = models.FloatField()
    feature23 = models.FloatField()
    feature24 = models.FloatField()
    feature25 = models.FloatField()



class Label(models.Model):
    feature = models.OneToOneField(Feature, on_delete=models.CASCADE)
    label1 = models.FloatField()
    label2 = models.FloatField()
    label3 = models.FloatField()
    label4 = models.FloatField()
    label5 = models.FloatField()
    label6 = models.FloatField()