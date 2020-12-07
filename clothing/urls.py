from django.urls import path
from . import views

urlpatterns = [
    path('women',views.women,name='women'),
]
