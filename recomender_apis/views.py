from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .models import QualityData, Product, User
from .serializers import QualityDataSerializer
from .serializers import UserSerializer, ProductSerializer

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView


# Create your views here.


class QualityDataViewSet(viewsets.ModelViewSet):
    queryset = QualityData.objects.all()
    serializer_class = QualityDataSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            if self.request.user.role != 'profesor':
                self.permission_denied(self.request)

        return super().get_permissions()


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [JWTAuthentication]

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            if self.request.user.role not in ['profesor', 'cliente']:
                self.permission_denied(self.request)

        return super().get_permissions()


class CustomTokenObtainPairView(TokenObtainPairView):
    pass
