from django.urls import path
from . import views
app_name = 'user'
urlpatterns = [
    #path('index/', views.index, name='index'),
    path('calculate/',views.calculate,name='calculate')
]