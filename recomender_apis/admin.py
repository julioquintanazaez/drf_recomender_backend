from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import User, Product, QualityData
	
admin.site.register(User)
admin.site.register(Product)
admin.site.register(QualityData)

