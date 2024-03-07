from django.contrib import admin
from django.urls import path
from products.views import index,index1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index),
    path('index1/',index1),
]