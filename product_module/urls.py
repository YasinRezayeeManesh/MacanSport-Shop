from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product_detail'),
    path('cat/<str:category>', views.ProductListView.as_view(), name='product_category'),
    path('cat-m/<str:main_category>', views.ProductListView.as_view(), name='product_category_main'),
    path('product-comment/', views.send_product_comment, name='product_comment'),
    path('search/', views.search, name='search'),
]
