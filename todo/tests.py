from django.urls import resolve
from django.test import TestCase

from todo.views import todo_view


class TodoAPIViewTest(TestCase):
    def test_todo_api_url_to_todo_view(self):
        found = resolve("/api/todo/")
        self.assertEqual(found.func, todo_view)
