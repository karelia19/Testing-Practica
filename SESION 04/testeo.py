import unittest
import requests

class TestRequests(unittest.TestCase):

    def test_get_status_code(self):
        response = requests.get('https://www.google.com')
        self.assertEqual(response.status_code, 200)

    def test_get_content_type(self):
        response = requests.get('https://www.google.com')
        self.assertTrue(response.headers['Content-Type'].startswith('text/html'))

    def test_post_invalid_url(self):
        with self.assertRaises(requests.exceptions.MissingSchema):
            requests.post('invalid_url')

if __name__ == '__main__':
    unittest.main()