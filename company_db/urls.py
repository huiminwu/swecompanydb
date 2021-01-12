from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='proj-home'),
    path('exported/', views.export_csv, name="proj-exp"),
    path('about/', views.about, name="proj-about")
]