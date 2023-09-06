from django.shortcuts import render

from rest_framework import viewsets,status

from api_auth.models import ProductReview,Product

from api_auth.serializers import ProductReviewSerializer,ProductSerializer,RegistrationSerializer

from rest_framework.permissions import IsAuthenticated,AllowAny,IsAuthenticatedOrReadOnly,IsAdminUser

from api_auth.permissions import ReviewerOrReadOnly,AdminOrReadOnly

from rest_framework.views import APIView

from rest_framework.response import Response


from rest_framework.authtoken.models import Token

from . import signals

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters

from api_auth.pagination import ProductPagination

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AdminOrReadOnly]
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['name']
    # just add minus in query to get descending ordering
    filter_backends= [filters.OrderingFilter]
    ordering_fields = ['price']
    pagination_class = ProductPagination

class ProductReviewViewSet(viewsets.ModelViewSet):
    # queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
    permission_classes = [ReviewerOrReadOnly]
    queryset = ProductReview.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['rating','product']
    # def get_queryset(self):
    #     queryset = ProductReview.objects.all()
    #     username = self.request.query_params.get('username')
    #     if username is not None:
    #         queryset = queryset.filter(user__username__icontains=username)
    #     return queryset
    
    
    
class RegistrationView(APIView):
    def post(self,request):
        data = {}
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'Registration Successful'
            data['username'] = account.username
            data['email'] = account.email
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data=data)
    
    
    
class LogOutView(APIView):
    def post(self,request):
       request.user.auth_token.delete()
       return Response(data={'response':'token deleted successfully'},status=status.HTTP_200_OK)
        