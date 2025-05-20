

from django.urls import path
from rest_framework.routers import DefaultRouter
from .views_api import ProjectViewSet, TokenLoginView, MyOffersAPIView


router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')

urlpatterns = router.urls + [
    path('api/token/', TokenLoginView.as_view(), name='token_login'),
    path('my-offers/', MyOffersAPIView.as_view(), name='my_offers_api'),
]

