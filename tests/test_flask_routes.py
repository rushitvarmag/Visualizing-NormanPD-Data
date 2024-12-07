import unittest
from main import app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Upload Your PDF File', response.data)

    def test_visualize_page(self):
        response = self.app.get('/visualize')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Select Visualization Type', response.data)
