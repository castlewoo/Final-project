# serializers

from rest_framework import serializers
from .models import RestaurantInfo, FoodInfoWithTaboo

class RestaurantInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantInfo
        fields = [
            "food",
            "store_name",
            "addr",
            "tel",
            "y좌표",
            "id",
        ]


class foodInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodInfoWithTaboo
        fields = [
            "food",
            "info",
            "ingredient",
            "taboo_ingredient",
        ]
