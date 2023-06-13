from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_all, name='learn_all'),
    path('<int:id>', views.index, name='learn'),
    path('<int:id>/cards', views.cards, name='cards'),    
]