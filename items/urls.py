from django.urls import path
from items import views

urlpatterns = [
    path("", views.item_index, name="item_index"),
    path("<int:pk>/", views.item_detail, name="item_detail"),
    path("cart/", views.view_cart, name="view_cart"),
    path('add/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
]