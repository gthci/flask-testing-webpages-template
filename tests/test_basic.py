import unittest, sys

sys.path.append('../flask-testing-webpages-template') # imports python file from parent directory
from app import app #imports flask app object

class BasicTests(unittest.TestCase):

    # executed prior to each test
    def setUp(self):
        self.app = app.test_client()

    ###############
    #### tests ####
    ###############

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_home_page(self):
        response = self.app.get('/home', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'This is the home page', response.data)

if __name__ == "__main__":
    unittest.main()