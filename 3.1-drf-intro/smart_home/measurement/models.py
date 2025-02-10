from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()


class Measurement(models.Model):
    id = models.BigAutoField(primary_key=True)
    temperature = models.FloatField()
    created_at = models.TimeField(auto_now=True, auto_now_add=True)
