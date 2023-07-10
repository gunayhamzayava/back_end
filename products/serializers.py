from rest_framework import serializers
from .models import Test

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.FloatField()


class TestProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"
