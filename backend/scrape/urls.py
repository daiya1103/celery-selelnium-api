from django.urls import path, include
from . import views

urlpatterns = [path("", views.task_1, name="task_1")]
