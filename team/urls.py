from django.urls import path
from . import views

urlpatterns = [
    path('', views.teamPage, name='team'),
    path('<str:slug>', views.detailPage, name='detail')
]