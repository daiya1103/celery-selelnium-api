from django.shortcuts import render
from .serializers import (
    UserCreationSerializer,
    UserSerializer,
    RecipeSerializer,
    KeywordPostSerializer,
    CommonSettingSerializer,
    MercariSerializer,
    YahooSerializer,
    PaypaySerializer,
    RakumaSerializer,
)
from scrape.models import (
    Amazon,
    Mercari,
    Rakuma,
    Yahoo,
    Paypay,
    Recipe,
    Keyword,
    Common,
)
from .custom_permissions import UserPermission, KeywordPermission

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
)
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status


# Create your views here.


class UserCreateView(CreateAPIView):
    serializer_class = UserCreationSerializer


class UserView(APIView):
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        data = serializer.data

        return Response(data, status=status.HTTP_200_OK)


class RecipeViewset(ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
    permission_classes = (UserPermission,)
    authentication_classes = (JWTAuthentication,)

    def get_queryset(self):
        user = self.request.user
        return Recipe.objects.filter(user=user)


class KeywordViewSet(ModelViewSet):
    serializer_class = KeywordPostSerializer
    queryset = Keyword.objects.all()
    permission_classes = (KeywordPermission,)
    authentication_classes = (JWTAuthentication,)

    def get_queryset(self):
        user = self.request.user
        return Keyword.objects.filter(recipe__user=user)


class CommonViewSet(ModelViewSet):
    serializer_class = CommonSettingSerializer
    queryset = Common.objects.all()
    permission_classes = (UserPermission,)
    authentication_classes = (JWTAuthentication,)

    def get_queryset(self):
        user = self.request.user
        return Common.objects.filter(user=user)

    def destroy(self, request, *args, **kwargs):
        response = {"message": "設定は削除できません"}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class MercariViewSet(ModelViewSet):
    serializer_class = MercariSerializer
    queryset = Mercari.objects.all()
    permission_classes = (UserPermission,)
    authentication_classes = (JWTAuthentication,)

    def get_queryset(self):
        user = self.request.user
        return Mercari.objects.filter(user=user)

    def destroy(self, request, *args, **kwargs):
        response = {"message": "設定は削除できません"}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
