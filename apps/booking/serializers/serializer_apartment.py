from rest_framework import serializers
from apps.booking.models.apartments import Apartment

class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = '__all__'

