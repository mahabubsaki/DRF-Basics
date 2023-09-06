from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import BookViewSet
from rest_framework.authtoken.views import obtain_auth_token

# Create a router and register our viewsets with it.
router = DefaultRouter()

#we dont need this on method 2 generic
router.register(r'books', BookViewSet,basename="book")


# The API URLs are now determined automatically by the router.
urlpatterns = [
    # path('books/', BookListView.as_view()),
    # path('books/<int:pk>/', BookListUpdateDelete.as_view()),
    # path('books/', GenericBookList.as_view()),
    # path('books/<int:pk>/', GenericBookDetail.as_view()),
    path('',include(router.urls)),
   
]