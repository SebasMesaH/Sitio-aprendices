from django.urls import path
from .import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('agregar',views.agregar, name='agregar'),
    path('aprendices', views.aprendices, name='aprendices'),
    path('editar/<int:id>', views.editar, name='editar'),


    path('eliminar/<int:id>',views.eliminar, name='eliminar'),



]