import unittest
from run import app


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_query(self):
        response = self.app.post('/query', data=dict(query='SELECT 1'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'1', response.data)


if __name__ == '__main__':
    unittest.main()
