import unittest
from app import app

class TestApp(unittest.TestCase):
    """Test cases for the Flask application."""
    
    def setUp(self):
        """Set up the test client."""
        self.app = app.test_client()
        self.app.testing = True
    
    def test_hello_endpoint(self):
        """Test the root endpoint returns the correct message."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), "Hello from Python!")

if __name__ == '__main__':
    unittest.main()
