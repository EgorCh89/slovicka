from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_all, name='learn_all'),
    path('<str:name>', views.index, name='learn'),
    path('<str:name>/cards', views.cards, name='cards'),    
]