from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from django.contrib.auth import authenticate

from .models import Project, Offer
from .serializers import ProjectSerializer, OfferSerializer
from .token import get_tokens_for_user


class TokenLoginView(APIView):
    """
    API endpoint для входа пользователя и получения JWT токенов.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user:
            tokens = get_tokens_for_user(user)
            return Response(tokens)
        return Response({"error": "Invalid credentials"}, status=400)


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint для работы с проектами.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class MyOffersAPIView(ListAPIView):
    """
    Возвращает список откликов текущего пользователя.
    """
    serializer_class = OfferSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Offer.objects.filter(freelancer=self.request.user)


