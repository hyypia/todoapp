from django.urls import path

from todo import views


urlpatterns = [
    path("todo/", views.todo_item),
]
