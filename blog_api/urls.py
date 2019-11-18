from django.conf.urls import url
from django.urls import path,include
from rest_framework import routers
from . views import HomeView,LoginView

from . import views

router = routers.DefaultRouter()
router.register(r'login', LoginView, basename = 'login')
router.register(r'',  HomeView, basename = 'home')


urlpatterns = [
                    url(r'', include(router.urls)),
              ]




