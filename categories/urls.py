from django.urls import path
from .views import CategoryListCreateView,CategorySearchView


urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/search/', CategorySearchView.as_view(), name='category-search'),
]
