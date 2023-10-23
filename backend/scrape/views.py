from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from .tasks import task_2
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from user.serializers import RecipeSerializer
from .models import (
    Amazon,
    Mercari,
    Rakuma,
    Yahoo,
    Paypay,
    Recipe,
    Keyword,
)

# Create your views here.


def task_1(request):
    task = task_2.apply_async()
    return HttpResponse(task.id)
