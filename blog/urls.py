from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('<int:id_post>/', views.detalhe, name='detalhe'),
]