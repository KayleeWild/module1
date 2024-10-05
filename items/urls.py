from django.urls import path
from items import views

urlpatterns = [
    path("", views.item_index, name="item_index"),
    path("<int:pk>/", views.item_detail, name="item_detail"),
]