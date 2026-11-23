from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Secciones informativas
    path('como-hacerla/', views.como_hacer, name='como_hacer'),
    path('materiales/', views.materiales, name='materiales'),
    path('beneficios/', views.beneficios, name='beneficios'),
    path('preguntas/', views.preguntas, name='preguntas'),

    # Créditos de las fotos
    path('creditos/', views.creditos, name='creditos'),
]
