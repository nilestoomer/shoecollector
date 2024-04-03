from rest_framework import serializers
from .models import Shoe, Wear

class ShoeSerializer(serializers.ModelSerializer):
    wear_for_today = serializers.SerializerMethodField()

    class Meta:
        model = Shoe
        fields = '__all__'

    def get_wear_for_today(self, obj):
        return obj.wear_for_today()

class WearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wear
        fields = '__all__'
        read_only_fields = ('shoe',)