
from django.urls import path
from store import views
urlpatterns = [
    #path('', views.storeOverview, name='storeOverview'),
    path('product-list/', views.showAllProducts, name='product-list'),
    #path('product-filter/', views.ProductListApi.as_view(), name='product-filter'),
    path('product-detail/<int:pk>/', views.viewProduct, name='product-detail'),
    path('product-create/', views.createProduct, name='product-create'),
    path('product-update/<int:pk>/', views.updateProduct, name='product-update'),
    path('product-delete/<int:pk>/', views.deleteProduct, name='product-delete'),

    path('category-list/', views.showAllCategories, name='category-list'),
    path('category-detail/<int:pk>/', views.viewCategory, name='category-detail'),
    path('category-create/', views.createCategory, name='category-create'),
    path('category-update/<int:pk>/',
         views.updateCategory, name='category-update'),
    path('category-delete/<int:pk>/',
         views.deleteCategory, name='category-delete'),
]
