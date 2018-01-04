# from django.test import TestCase
# from .models import Users
# import requests
# from django.test.client import encode_multipart, RequestFactory
#
#
# base_url = "http://localhost:8000"
#
#
# class PingTestCase(TestCase):
#     def test1(self):
#         """
#         Test case for ping
#         """
#         resp = self.client.get('/api/v1/ping/')
#         self.assertEqual(eval(resp.content), dict(response='pong', status=200))
#
#
# class UserTestCase(TestCase):
#     def test1(self):
#         user = Users.objects.create(firstName='Agrim', lastName='Sharma', password='Chetu@123',email='test@g.com')
#         user.save()
#         self.assertEqual(user.get_full_name(), "Agrim Sharma")
#
#     def test2(self):
#         response = requests.get(base_url + "/api/v1/users/2/")
#         self.assertEquals(eval(response._content),
#                           dict(firstName="Rohit",lastName="Khanna", email="rohit.khanna@gmail.com",role="Doctor",
#                                updatedDate="2017-12-08T06:09:01Z"))
