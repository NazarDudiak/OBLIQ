from rest_framework import serializers
from .models import OrderImage


class OrderImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderImage
        fields = "__all__"
