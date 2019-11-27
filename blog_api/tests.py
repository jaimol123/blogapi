from django.urls import path,include, reverse
from . models import UserProfiles , Recipe, Comments,Contact
from . views import HomeView, CommentListView, LoginView,ContactView
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

# factory = APIRequestFactory()
# user = UserProfiles.objects.get(username = 'jiss')
# view = HomeView
# request = factory.get('/home/')
# print(request)
# print("-------------",force_authenticate(request, user = user))
# request_login = factory.get('/login-list/')
# request_signup = factory.get('home')
# request_contactpost = factory.post('/contact/', {'name' : 'jaimol', 'email' : 'jai@gmail.com', 'msg' : 'abc', 'subject' : '12'})
# print(request_contactpost)
# request_slider = factory.get('/slider/')
# request_socialLinks = factory.get('/socialLinks/')
# request_footerimage = factory.get('/footerimage/')
# print(request_footerimage)
#
# request = factory.patch('/comment_update/', {'name' : 'jenifer'})
# request = factory.get('/recipe-list/', {'recipe_name' : 'pizza'})
#
# client = APIClient()
# response = client.login(username = 'jiss', password = 'jiss')
# print(response)
# response = client.logout
# print("logout-----", response)
# client = RequestsClient()
# response = client.get('http://testserver/api/v1/comment-list/')
# print(response)
# assert response.status_code == 200


# class TokenTest(APITestCase):
#
#        def setUp(self):
#               self.factory = APIRequestFactory()
#               self.user = self.setup_user()
#               self.token = Token.objects.create(user = self.user)
#               self.token.save()
#               self.view = HomeView.as_view({'post' : 'create'})
#               self.uri = '/api/v1/'
#
#        @staticmethod
#        def setup_user():
#               UserProfiles = get_user_model()
#               return UserProfiles.objects.create_user(first_name = 'jai', username = 'jai', password = 'jai', email = 'jai@gmail.com')
#
#        def test_token(self):
#               request = self.factory.get(self.uri, HTTP_AUTHORIZATION='Token {}'.format(self.token.key))
#               request.user = self.user
#               response = self.view(request)
#               self.assertEqual(response.status_code, 200)

class LoginTest(APITestCase):

    def setUp(self):

        self.client = APIClient()
        #self.view = LoginView.as_view({'post' : 'create'})
        self.uri = '/api/v1/login-post/'

    def test_login_post(self):

        print(self.client.login(username = 'riya', password = 'riya'))
        request = self.client.post(self.uri)
        #response = self.view(request)
        self.assertEqual(request.status_code,200)


class TestAll(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = CommentListView.as_view({'get': 'list'})
        self.uri = '/api/v1/comment-list/'

    def test_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 200)