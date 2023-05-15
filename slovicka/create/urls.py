from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<str:name>', views.edit, name='index'),
    path('new/', views.create_new, name='new'),
]