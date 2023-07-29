from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    path("", views.APIOverview.as_view()),
    path("task-list/", views.TasksView.as_view()),
    path("task-list/<str:pk>/", views.TaskDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
