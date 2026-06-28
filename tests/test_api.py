import unittest

from app import create_app


class TodoApiTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app().test_client()

    def test_get_valid_todo(self):
        response = self.app.get("/todos/1")

        self.assertEqual(response.status_code, 200)

    def test_get_invalid_todo(self):
        response = self.app.get("/todos/999")

        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()