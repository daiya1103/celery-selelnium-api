from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter, SimpleRouter

router = DefaultRouter()

router.register("recipe", views.RecipeViewset, basename="recipe")
router.register("keyword", views.KeywordViewSet, basename="keyword")
router.register("common", views.CommonViewSet, basename="common")
router.register("mercari", views.MercariViewSet, basename="mercari")
router.register("yahoo", views.YahooViewSet, basename="yahoo")
router.register("rakuma", views.RakumaViewSet, basename="rakuma")
router.register("paypay", views.PayPayViewSet, basename="paypay")
router.register("ngword", views.NgWordViewSet, basename="ngword")
router.register("exclusion", views.ExculsionViewSet, basename="exclusion")
router.register("replace", views.ReplaceViewSet, basename="replace")
router.register("deleteword", views.DeleteViewSet, basename="deleteword")
router.register("staff", views.UserViewSet, basename="staff")
router.register("amazon", views.AmazonViewSet, basename="amazon")
router.register("default_margin", views.DefaultMarginViewSet, basename="default_margin")
router.register("margin", views.MarginViewSet, basename="margin")

urlpatterns = [
    path("create/", views.UserCreateView.as_view(), name="user-create"),
    path("get/", views.UserView.as_view(), name="user-get"),
    path("ngsetting/", views.NgSettingView.as_view(), name="ngsetting"),
    path("main_info/", views.NgSettingView.as_view(), name="ngsetting"),
    path("", include(router.urls)),
]
