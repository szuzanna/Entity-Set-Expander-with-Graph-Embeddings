from django.urls import path
from search_similar import views

urlpatterns = [
    path('', views.main, name='main'),
    path('show/', views.show_results, name='show_results'),
]