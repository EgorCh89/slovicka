from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='create'),
    path('new',views.create_new,name="new_dict"),
    path('<str:name>/edit', views.edit, name='edit'),
    
]