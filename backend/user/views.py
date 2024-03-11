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
    NgSettingSerializer,
    MainInfomationSerializer,
    NgwordSerializer,
    ReplaceSerializer,
    ExclusionSerializer,
    DeleteSerializer,
    AmazonSerializer,
    MarginSerializer,
    DefaultMarginSerializer,
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
    Ngword,
    Replace,
    Exclusion,
    Delete,
    DefaultMargin,
    Margin
)
from django.contrib.auth import get_user_model

from .custom_permissions import UserPermission, KeywordPermission, StaffPermission
from rest_framework.permissions import AllowAny

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
    permission_classes = (AllowAny,)


class UserView(APIView):
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        data = serializer.data

        return Response(data, status=status.HTTP_200_OK)


class NgSettingView(APIView):
    permission_classes = (UserPermission,)
    authentication_classes = (JWTAuthentication,)

    def get(self, request):
        user = request.user
        serializer = NgSettingSerializer(user)
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


class AmazonViewSet(ModelViewSet):
    serializer_class = AmazonSerializer
    queryset = Amazon.objects.all()
    permission_classes = (UserPermission,)
    authentication_classes = (JWTAuthentication,)

    def get_queryset(self):
        user = self.request.user
        return Amazon.objects.filter(user=user)

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


class YahooViewSet(ModelViewSet):
    serializer_class = YahooSerializer
    queryset = Yahoo.objects.all()
    permission_classes = (UserPermission,)
    authentication_classes = (JWTAuthentication,)

    def get_queryset(self):
        user = self.request.user
        return Yahoo.objects.filter(user=user)

    def destroy(self, request, *args, **kwargs):
        response = {"message": "設定は削除できません"}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

class RakumaViewSet(ModelViewSet):
    serializer_class = RakumaSerializer
    queryset = Rakuma.objects.all()
    permission_classes = (UserPermission,)
    authentication_classes = (JWTAuthentication,)

    def get_queryset(self):
        user = self.request.user
        return Rakuma.objects.filter(user=user)

    def destroy(self, request, *args, **kwargs):
        response = {"message": "設定は削除できません"}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

class PayPayViewSet(ModelViewSet):
    serializer_class = PaypaySerializer
    queryset = Paypay.objects.all()
    permission_classes = (UserPermission,)
    authentication_classes = (JWTAuthentication,)

    def get_queryset(self):
        user = self.request.user
        return Paypay.objects.filter(user=user)

    def destroy(self, request, *args, **kwargs):
        response = {"message": "設定は削除できません"}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class NgSettingView(APIView):
    permission_classes = (UserPermission,)
    authentication_classes = (JWTAuthentication,)

    def get(self, request):
        user = request.user
        serializer = MainInfomationSerializer(user)
        data = serializer.data

        return Response(data, status=status.HTTP_200_OK)


class NgWordViewSet(ModelViewSet):
    permission_classes = (UserPermission,)
    authentication_classes = (JWTAuthentication,)
    queryset = Ngword.objects.all()
    serializer_class = NgwordSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data["user"] = self.request.user.id
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        else:
            print(serializer.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ExculsionViewSet(ModelViewSet):
    permission_classes = (UserPermission,)
    authentication_classes = (JWTAuthentication,)
    queryset = Exclusion.objects.all()
    serializer_class = ExclusionSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data["user"] = self.request.user.id
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        else:
            print(serializer.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ReplaceViewSet(ModelViewSet):
    permission_classes = (UserPermission,)
    authentication_classes = (JWTAuthentication,)
    queryset = Replace.objects.all()
    serializer_class = ReplaceSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data["user"] = self.request.user.id
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        else:
            print(serializer.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class DeleteViewSet(ModelViewSet):
    permission_classes = (UserPermission,)
    authentication_classes = (JWTAuthentication,)
    queryset = Delete.objects.all()
    serializer_class = DeleteSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data["user"] = self.request.user.id
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        else:
            print(serializer.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(ModelViewSet):
    permission_classes = (StaffPermission,)
    authentication_classes = (JWTAuthentication,)
    queryset = get_user_model().objects.all()
    serializer_class = UserCreationSerializer


class DefaultMarginViewSet(ModelViewSet):
    permission_classes = (StaffPermission,)
    authentication_classes = (JWTAuthentication,)
    queryset = DefaultMargin.objects.all()
    serializer_class = DefaultMarginSerializer

    def get_queryset(self):
        user = self.request.user
        return DefaultMargin.objects.filter(user=user)

    def destroy(self, request, *args, **kwargs):
        response = {"message": "設定は削除できません"}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

class MarginViewSet(ModelViewSet):
    permission_classes = (StaffPermission,)
    authentication_classes = (JWTAuthentication,)
    queryset = Margin.objects.all()
    serializer_class = MarginSerializer

    def get_queryset(self):
        user = self.request.user
        return Margin.objects.filter(user=user)

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data["user"] = self.request.user.id
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        else:
            print(serializer.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST)