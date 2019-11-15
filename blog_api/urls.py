from django.conf.urls import url
from django.urls import path,include
from rest_framework import routers

from . import views


urlpatterns = [
                url(r'', views.HomeView.as_view()),
                url(r'auth', include('rest_auth.urls'))

]