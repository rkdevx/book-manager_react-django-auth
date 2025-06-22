
import book_api.views as views
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('books/', views.book_list, name='book-list'),
    path('books/<int:pk>/', views.book_detail, name='book-detail'),
    path('register/', views.register_user),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('google-login/', views.google_login),
]
