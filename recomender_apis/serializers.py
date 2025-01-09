from rest_framework import serializers
from django.contrib.auth.models import User
from .models import QualityData, Product, User

class QualityDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityData
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
	

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

