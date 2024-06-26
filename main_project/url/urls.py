from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/<str:short_url>/', views.redirect_url,name='redirect_url'),
    path('dashboard/<slug:url_slug>/',views.redirect_slug,name='redirect_slug'),
    path('delete/<int:url_id>/', views.delete_url, name='delete_url'),
]