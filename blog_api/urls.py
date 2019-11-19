from django.conf.urls import url
from django.urls import path,include
from rest_framework import routers
from . views import HomeView, LoginView, ContactView, RecipeView,  SliderView, SocialLinkView, FooterImageView,FeatureView, NewsletterView,AddressView

from . import views

router = routers.DefaultRouter()
router.register(r'address', AddressView, basename = 'address'),
router.register(r'newsletter', NewsletterView, basename = 'newsletter')
router.register(r'feature', FeatureView , basename = 'feature')
router.register(r'footerimage', FooterImageView, basename = 'footerimage')
router.register(r'socialLinks', SocialLinkView, basename = 'socialLinks')
router.register(r'slider', SliderView, basename = 'slider')
router.register(r'recipe', RecipeView, basename = 'recipe')
router.register(r'contact', ContactView, basename = 'contact')
router.register(r'login', LoginView, basename = 'login')
router.register(r'',  HomeView, basename = 'home')





urlpatterns = [
                    url(r'', include(router.urls)),
              ]




