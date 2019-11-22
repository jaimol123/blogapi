from django.conf.urls import url
from django.urls import path,include
from rest_framework import routers
from . views import HomeView, LoginView, ContactView, RecipeView,  SliderView, SocialLinkView, FooterImageView,FeatureView, NewsletterView,AddressView,CommentsView, RatingView,RecipePostView,CommentListView,CommentUpdateView

from . import views

router = routers.DefaultRouter()
router.register(r'comment_update' , CommentUpdateView, basename = 'comment_update')
router.register(r'comment_list', CommentListView, basename = 'comment_list')
router.register(r'recipe_post', RecipePostView , basename = 'recipe_post'),
router.register(r'rate_post' , RatingView , basename = 'rating'),
router.register(r'comment_post', CommentsView, basename = 'comment'),
router.register(r'address_list', AddressView, basename = 'address'),
router.register(r'newsletter_post', NewsletterView, basename = 'newsletter')
router.register(r'feature_list', FeatureView , basename = 'feature')
router.register(r'footerimage_list', FooterImageView, basename = 'footerimage')
router.register(r'socialLinks_list', SocialLinkView, basename = 'socialLinks')
router.register(r'slider_list', SliderView, basename = 'slider')
router.register(r'recipe_list', RecipeView, basename = 'recipe')
router.register(r'contact_post', ContactView, basename = 'contact')
router.register(r'login_post', LoginView, basename = 'login')
router.register(r'',  HomeView, basename = 'home')





urlpatterns = [
                    url(r'', include(router.urls)),
              ]




