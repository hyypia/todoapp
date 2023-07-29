from django.urls import resolve
from django.test import TestCase
from rest_framework.test import APIClient

from todo.views import todo_item


class TodoAPIViewTest(TestCase):
    def test_todo_api_url_to_todo_view(self) -> None:
        found = resolve("/api/todo/")
        self.assertEqual(found.func, todo_item)


class TestTodoAPI(TestCase):
    def setUp(self) -> None:
        self.client = APIClient(enforce_csrf_checks=True)

    def test_create_todo(self) -> None:
        url = "/api/todo/"
        data = {
            "title": "Create backend for client todo app",
            # "complited": False,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.content.decode("utf-8"), "Create backend for client todo app"
        )
        # self.assertEqual(response.json()["complited"], False)

    def test_get_todo(self) -> None:
        url = "/api/todo/"
        # response = requests.get(url + "todo/")
        # self.assertEqual(response.status_code, 200)

    def test_update_todo(self) -> None:
        pass

    def test_delete_todo(self) -> None:
        pass
