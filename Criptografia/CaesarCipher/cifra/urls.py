from django.urls import path
from .views import cifra_view

urlpatterns = [
    path('', cifra_view, name='cifra_view'),
]
