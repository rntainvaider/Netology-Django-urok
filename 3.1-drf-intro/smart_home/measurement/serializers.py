from rest_framework import serializers

from measurement.models import Measurement, Sensor

# TODO: опишите необходимые сериализаторы


class MeasurementSerilizer(serializers.Serializer):
    class Meta:
        model = Measurement
        fields = ["id", "temperature", "created_at"]


class SensorSerializer(serializers.Serializer):
    measurements = MeasurementSerilizer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ["id", "name", "description"]
