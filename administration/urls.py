
from django.urls import path
from .views import index

app_name = 'administration'

urlpatterns = [
    path('', index, name='index'),
]
