from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import BookViewSet, PublisherViewSet, register_user, login_user

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'publishers', PublisherViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
