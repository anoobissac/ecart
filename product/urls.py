
from django.urls import path
from product.views import ProductDetailView, ProductListView,CategoryListView,CategoryDetailView,ProductCreateView,ProductUpdateView,ProductDeleteView,CategoryCreateView,CategoryDeleteView,CategoryUpdateView,ProductListByCategory,SearchView

urlpatterns=[
    path('create/',ProductCreateView.as_view(),name="product_create"),
    path("list/",ProductListView.as_view(),name="product_list"),
    path("<int:pk>/detail/",ProductDetailView.as_view(),name="product_detail"),
    path('<int:pk>/update/',ProductUpdateView.as_view(),name='product_update'),
    path('<int:pk>/delete/',ProductDeleteView.as_view(),name='product_delete'),
    path('category/create/',CategoryCreateView.as_view(),name="category_create"),
    path("category/list/",CategoryListView.as_view(),name="category_list"),
    path('category/<int:pk>/detail/',CategoryDetailView.as_view(),name="category_detail"),
    path('category/<int:pk>/update/',CategoryUpdateView.as_view(),name='category_update'),
    path('category/<int:pk>/delete/',CategoryDeleteView.as_view(),name='category_delete'),
    path('<int:pk>/searchlist/', ProductListByCategory.as_view(),name="searchlist"),
    path('search/',SearchView.as_view(),name='search_product'),
]