from django.urls import path,include, reverse
from . models import UserProfiles , Recipe, Comments,Contact,Newsletter
from . views import HomeView, CommentListView, LoginView,ContactView,RecipePostView,NewsletterView,CommentsView,CommentUpdateView,RecipeView,RatingView,RatingListView,SliderView,SocialLinkView,FooterImageView,FeatureView,AddressView
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token



class TestCommentList(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = CommentListView.as_view({'get': 'list'})
        self.uri = '/api/v1/comment-list/'

    def test_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 200)


class TestCommentPost(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.uri = '/api/v1/'
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user('testuser', id=85214, email='test@gmail.com', password='testuser')

    def test_create(self):
        request = self.client.get(self.uri, HTTP_AUTHORIZATION='Token {}'.format(self.token.key))
        request.user = self.user
        self.client.login(username = request.user.username , password = request.user.password)
        response = self.client.post('/api/v1/comment-post/', {'name' : 'jiss', 'msg' : 'abc', 'subject' : 'ab', 'receipe_name_id' : 2})
        self.assertEqual(request.status_code, 200)


class TestCommentUpdate(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = CommentUpdateView.as_view({'update' : 'patch'})
        self.url = '/api/v1/comment-update/6'

    def test_update(self):
        request = self.factory.patch(self.url, {'name' : 'jismol', 'msg' : 'abc222', 'subject' : 'ab',})
        response = self.view(request)
        self.assertEqual(response.status_code, 201)


class TestContact(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = ContactView.as_view({'post' : 'create'})
        self.url = '/api/v1/contact-post/'

    def test_create(self):
        request = self.factory.post(self.url, {'contact_name' : 'anc', 'contact_subject' : 'jj', 'contact_message' : 'bb', 'contact_email' : 'g@gmail.com'})
        response = self.view(request)
        self.assertEqual(response.status_code, 200)


class TestRecipeList(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = RecipeView.as_view({'get': 'list'})
        self.url = '/api/v1/recipe-list/'

    def test_list(self):
        request = self.factory.get(self.url)
        response = self.view(request)
        self.assertEqual(response.status_code, 200)


class TestRecipePost(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = RecipePostView.as_view({'post' :'create'})
        self.url = '/api/v1/recipe-post/'

    def test_create(self):
        request = self.factory.post(self.url, {'recipe_name ' : 'fish', 'type' : 'lunch', 'category' : 'nonveg'})
        response = self.view(request)
        self.assertEqual(response.status_code, 200)


class TestNewsletter(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view =  NewsletterView.as_view({'post' : 'create'})
        self.url = '/api/v1/newsletter-post/'

    def test_create(self):
        request = self.factory.post(self.url, {'mail' : 'jai@gmail.com'})
        response = self.view(request)
        self.assertEqual(response.status_code, 200)


class TestRatingPost(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = RatingView.as_view({'post' : 'create'})
        self.url = '/api/v1/rate-post/'

    def test_create(self):
        request = self.factory.post(self.url, {'name' : 'jiss', 'rate' : 2, 'recipename' : 'fish'})
        response = self.view(request)
        self.assertEqual(response.status_code, 200)


class TestSlider(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view =  RatingListView.as_view({'get' : 'list'})
        self.url = 'api/v1/rate-list/'

    def test_list(self):
        request = self.factory.get(self.url)
        response = self.view(request)
        self.assertEqual(response.status_code, 200)


class TestSlider(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = SliderView.as_view({'get' : 'list'})
        self.url = 'api/v1/slider-list/'

    def test_list(self):
        request = self.factory.get(self.url)
        response = self.view(request)
        self.assertEqual(response.status_code, 200)


class TestSocialLinks(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = SocialLinkView.as_view({'get': 'list'})
        self.url = 'api/v1/socialLinks-list/'

    def test_list(self):
        request = self.factory.get(self.url)
        response = self.view(request)
        self.assertEqual(response.status_code, 200)


class TestFooterimage(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = FooterImageView.as_view({'get': 'list'})
        self.url = 'api/v1/footerimage-list/'

    def test_list(self):
        request = self.factory.get(self.url)
        response = self.view(request)
        self.assertEqual(response.status_code, 200)


class TestFeatures(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = FeatureView.as_view({'get': 'list'})
        self.url = 'api/v1/feature-list/'

    def test_list(self):
        request = self.factory.get(self.url)
        response = self.view(request)
        self.assertEqual(response.status_code, 200)


class TestAddress(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = AddressView.as_view({'get': 'list'})
        self.url = 'api/v1/address-list/'

    def test_list(self):
        request = self.factory.get(self.url)
        response = self.view(request)
        self.assertEqual(response.status_code, 200)





