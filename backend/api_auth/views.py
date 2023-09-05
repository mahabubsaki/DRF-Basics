from django.shortcuts import render

from rest_framework import viewsets

from api_auth.models import ProductReview,Product

from api_auth.serializers import ProductReviewSerializer,ProductSerializer

from rest_framework.permissions import IsAuthenticated,AllowAny,IsAuthenticatedOrReadOnly,IsAdminUser

from api_auth.permissions import ReviewerOrReadOnly

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductReviewViewSet(viewsets.ModelViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
    permission_classes = [ReviewerOrReadOnly]