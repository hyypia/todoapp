import requests
import unittest
import json


class TestTodoAPI(unittest.TestCase):
    def setUp(self) -> None:
        self.api_url = "http://localhost:8000/api/"

    def test_create_todo(self) -> None:
        data = {
            "title": "Create backend for client todo app",
            # "complited": False,
        }
        response = requests.post(self.api_url + "todo/", data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.text, "Create backend for client todo app")
        # self.assertEqual(response.json()["complited"], False)

    def test_get_todo(self) -> None:
        pass

    def test_update_todo(self) -> None:
        pass

    def test_delete_todo(self) -> None:
        pass


if __name__ == "__main__":
    unittest.main()
