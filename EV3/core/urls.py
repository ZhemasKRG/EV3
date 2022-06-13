from django.urls import path
from .views import home, quienes_somos, Form

urlpatterns = [
    path('',home, name="home"),
    path('quienes_somos/', quienes_somos, name="quienes_somos"),
    path('Form/', Form, name="Form"),
]