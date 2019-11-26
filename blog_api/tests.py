from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from django.test import TestCase
from . models import UserProfiles , Recipe, Comments
from rest_framework.test import APIClient, RequestsClient
from . views import HomeView

factory = APIRequestFactory()
user = UserProfiles.objects.get(username = 'jiss')
view = HomeView
request = factory.get('/home/')
print(request)
print("-------------",force_authenticate(request, user = user))

request_login = factory.get('/login-list/')
request_signup = factory.get('home')
request_contactpost = factory.post('/contact/', {'name' : 'jaimol', 'email' : 'jai@gmail.com', 'msg' : 'abc', 'subject' : '12'})
print(request_contactpost)
request_slider = factory.get('/slider/')
request_socialLinks = factory.get('/socialLinks/')
request_footerimage = factory.get('/footerimage/')
print(request_footerimage)

request = factory.patch('/comment_update/', {'name' : 'jenifer'})
request = factory.get('/recipe-list/', {'recipe_name' : 'pizza'})

client = APIClient()
response = client.login(username = 'jiss', password = 'jiss')
print(response)
response = client.logout
print("logout-----", response)
# client = RequestsClient()
# response = client.get('http://testserver/api/v1/comment-list/')
# print(response)
# assert response.status_code == 200



