from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('products/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart_view'),
    path('update-cart/<int:product_id>/', views.update_cart, name='update_cart'),  # НОВОЕ
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),  # НОВОЕ
    path('clear-cart/', views.clear_cart, name='clear_cart'),
]