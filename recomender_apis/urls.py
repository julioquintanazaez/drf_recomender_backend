from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QualityDataViewSet, UserViewSet, ProductViewSet, CustomTokenObtainPairView

router = DefaultRouter()
router.register(r'qualitydata', QualityDataViewSet)
router.register(r'users', UserViewSet)  # Añadir esta línea
router.register(r'products', ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
