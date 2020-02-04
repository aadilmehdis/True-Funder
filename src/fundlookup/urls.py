from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<int:pk>', views.profile, name='profile_with_pk'),
    path('pay/<int:pk>', views.pay, name='pay'),
    path('', include("django.contrib.auth.urls"))
]
