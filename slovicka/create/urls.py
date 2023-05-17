from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:name>', views.edit, name='dict'),
    path('dict/<str:name>/edit', views.create_new, name='edit'),
    path('newDict',views.create_new,name="new_dict")
]