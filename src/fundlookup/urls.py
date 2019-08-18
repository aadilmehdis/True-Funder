from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<int:pk>', views.profile, name='profile_with_pk'),
]
