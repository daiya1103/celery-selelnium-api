import json

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from .tasks import merscraper, indivisual_scraper
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView

from celery.result import AsyncResult

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from user.serializers import RecipeSerializer, ResearchResultSerializer
from .models import ResearchResult
from user.custom_permissions import UserPermission, KeywordPermission


# Create your views here.


class ScrapeView(APIView):
    authentication_classes = (JWTAuthentication,)

    def post(self, request, *args, **kwargs):
        data = request.data
        task = merscraper.apply_async(args=[data])

        response = {"message": "開始", "id": task.id}

        return Response(response, status=status.HTTP_202_ACCEPTED)

class IndivisualScrapeView(APIView):
    authentication_classes = (JWTAuthentication,)

    def post(self, request, *args, **kwargs):
        data = request.data
        task = indivisual_scraper.apply_async(args=[data])

        response = {"message": "開始", "id": task.id}

        return Response(response, status=status.HTTP_202_ACCEPTED)


class ResearchResultListView(APIView):
    authentication_classes = (JWTAuthentication,)

    def get(self, request):
        task_id = request.query_params.get("task_id", None)
        celery_task = AsyncResult(task_id)
        task_status = celery_task.status
        print(task_status)

        queryset = []
        result_data = []
        if task_id:
            queryset = ResearchResult.objects.filter(task_id=task_id)
            result_data = list(queryset.values())
            queryset.delete()

        res = {"results": result_data, "status": task_status}
        return Response(data=res, status=status.HTTP_200_OK)
