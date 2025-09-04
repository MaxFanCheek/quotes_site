from django.urls import path
from . import views

urlpatterns = [
    path('', views.random_quote, name='random'),
    path('top/', views.top_quotes, name='top'),
]
