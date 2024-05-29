from rest_framework import generics
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategorySearchView(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        queryset = Category.objects.filter(name__icontains=query)
        return queryset
