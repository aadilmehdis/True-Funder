from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<int:pk>', views.profile, name='profile_with_pk'),
    path('transfer/<int:pk>', views.transfer, name='transfer'),
    path('deposit/<int:pk>', views.deposit, name='deposit'),
    path('pay/<int:pk>', views.pay, name='pay'),
    path('ajax/load-vendor/', views.load_vendor, name='ajax_load_vendor'),
]
