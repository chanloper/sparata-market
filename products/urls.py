
from django.urls import path
from .views import ProductCreateView, ProductListView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('create/', ProductCreateView.as_view(), name='product-create'),
    path('<int:pk>/update/',
         ProductUpdateView.as_view(), name='product-update'),
    path('<int:pk>/delete/',
         ProductDeleteView.as_view(), name='product-delete'),
]
