from django.urls import path
from . import views  # Import views from the same directory

urlpatterns = [
    path('', views.index, name='index'),  # Define a URL pattern for the homepage
    path('search/', views.search, name='search'),  # Define a URL pattern for the search page   
    path('category/<str:category>/', views.category, name='category'),  # Define a URL pattern for the category 
    path('products/<str:sku>/', views.products, name='products'),  # Define a URL pattern for the category page
    
]
