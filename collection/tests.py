from django.test import TestCase

class CollectionTest(TestCase):
    def test_index(self):
        r = self.client.get('/')
        self.assertEqual(r.status_code, 200)

    def test_no_logic_page(self):
        r = self.client.get('/about/')
<<<<<<< HEAD
        self.assertEqual(r.status_code, 200)
=======
        self.assertEqual(r.status_code, 200)
>>>>>>> aad4790722e6696b5f765885d5268c03237b6492
