from django.test import TestCase
import json

class SchoolTest(TestCase):

    def test_enroll(self):
        resp = self.client.post(
            "/home",
            '{"f_name":"Giacomo","l_name":"Ferrari"}',
            content_type='application/json'
            )
        self.assertEqual(resp.status_code, 200)

    def test_search(self):
        resp = self.client.post(
            "/home",
            '{"f_name":"Giacomo","l_name":"Ferrari"}',
            content_type='application/json'
            )
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get('/home')
        self.assertEqual(resp.status_code,200)
        content = json.loads(resp.content)
        self.assertEqual(content[0]['f_name'], 'Giacomo')
        self.assertEqual(content[0]['l_name'], 'Ferrari')


