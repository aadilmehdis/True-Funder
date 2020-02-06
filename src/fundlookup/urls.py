from django.contrib.auth import views as auth_views
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<int:pk>', views.profile, name='profile_with_pk'),
    path('transfer/<int:pk>', views.transfer, name='transfer'),
    path('deposit/<int:pk>', views.deposit, name='deposit'),
    path('pay/<int:pk>', views.pay, name='pay'),
    path('analytics/<int:pk>', views.analytics, name='analytics'),
    path('ajax/load-vendor/', views.load_vendor, name='ajax_load_vendor'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='index'),
    path('', include("django.contrib.auth.urls"))
]
