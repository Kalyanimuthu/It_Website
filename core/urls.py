from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services_view, name='services'),
    path('projects/', views.projects, name='projects'),   # if you already have projects view
    path('team/', views.team, name='team'),               # if you have team view
    path('career/', views.career_view, name='career'),
    path('pricing/', views.pricing_view, name='pricing'),
    path('login/', views.login_view, name='login'),
    path('contact/', views.contact_view, name='contact'), # ensure contact_view exists
]
