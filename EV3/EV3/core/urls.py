from django.urls import path
from core import admin
from .views import home, quienes_somos, Form, productos


urlpatterns = [
    path('',home, name="home"),
    path('quienes_somos/', quienes_somos, name="quienes_somos"),
    path('Form/', Form, name="Form"),
    path('productos/', productos, name="productos"),
]
