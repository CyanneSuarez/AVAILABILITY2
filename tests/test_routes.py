# tests/test_routes.py

import unittest
from app import app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_list_by_availability(self):
        availability_status = "In Stock"
        response = self.app.get(f'/items?availability={availability_status}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'In Stock', response.data)

if __name__ == "__main__":
    unittest.main()
