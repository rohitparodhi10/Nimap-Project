from django.urls import path,include
from django.contrib import admin
urlpatterns = [
    path('nimap/',include('client.urls')),
    path('admin/',admin.site.urls)
]
