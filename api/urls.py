from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter  
from django.urls import include, path



from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

router = DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns = [

    path('token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('users/', views.UserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<uuid:pk>/', views.UserDetailAPIView.as_view(), name='user-detail'),

    path('services/', views.ServicesCreateAPIView.as_view(), name='user-detail'),
    path('services/<uuid:pk>/', views.ServicesDetailAPIView.as_view(), name='user-detail'),

    path('usedlist/', views.usedlistCreateAPIView.as_view(), name='user-detail'),
    path('usedlist/<uuid:pk>/', views.usedlistDetailAPIView.as_view(), name='user-detail'),

]