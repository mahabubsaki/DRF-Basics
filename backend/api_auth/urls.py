from django.urls import include,path
from rest_framework import routers
from api_auth.views import ProductReviewViewSet,ProductViewSet

router = routers.DefaultRouter()

router.register('products',ProductViewSet)
router.register('reviews',ProductReviewViewSet)


urlpatterns = [
    path('',include(router.urls))
]
