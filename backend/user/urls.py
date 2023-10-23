from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter, SimpleRouter

router = DefaultRouter()

router.register("recipe", views.RecipeViewset, basename="recipe")
router.register("keyword", views.KeywordViewSet, basename="keyword")
router.register("common", views.CommonViewSet, basename="common")
router.register("mercari", views.MercariViewSet, basename="mercari")

urlpatterns = [
    path("create/", views.UserCreateView.as_view(), name="user-create"),
    path("get/", views.UserView.as_view(), name="user-get"),
    path("", include(router.urls)),
]
