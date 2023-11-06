from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('verifier_parentheses2', views.verifier_parentheses2, name='verifier_parentheses2'),
]