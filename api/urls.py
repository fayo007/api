from django.urls import path
from . import views

urlpatterns = [
    path('product-list', views.list_products),
    path('product-detail/<int:id>/', views.product_detail),
    path('categorys', views.category_list),
    path('category-detail/<int:id>/', views.category_detail)
    # path('salom', views.salomlash)
]
