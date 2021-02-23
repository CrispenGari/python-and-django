
from django.urls import path

from . import views

urlpatterns =[
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('history/<int:hist_id>/', views.history, name='history'),
]