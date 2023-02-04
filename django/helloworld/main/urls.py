from django.urls import path

from main import views

urlpatterns = [
    path('index/', views.main_view),
    path('about/', views.about_view),
]
