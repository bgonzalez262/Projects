from django.urls import path
from . import views


app_name = 'vba'
urlpatterns = [
    path('', views.index, name='index'),
]