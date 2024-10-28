from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tutor/<int:tutor_id>/', views.tutor_profile, name='tutor_profile'),
]
