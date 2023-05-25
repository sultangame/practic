from django.urls import path
from . import views

urlpatterns = [
    path('', views.postPage, name='post'),
    path('post/<str:slug>/', views.detailPage, name='details')
]