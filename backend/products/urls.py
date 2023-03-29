from django.urls import path, include
from products import views
# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<

urlpatterns = [
    path('', views.user_products),
    path('all/', views.get_all_products),
    path('index/', views.index),
    path('upload/', views.uploadView),
]
