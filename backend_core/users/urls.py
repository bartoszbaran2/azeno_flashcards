
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CustomUserCreateView, BlackListTokenUpdate

app_name = 'users'

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', CustomUserCreateView.as_view(), name='register'),
    path('logout/', BlackListTokenUpdate.as_view(), name='logout'),
]


