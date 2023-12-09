from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.ScrapeView.as_view(), name="scrape"),
    path("result/", views.ResearchResultListView.as_view(), name="result"),
]
