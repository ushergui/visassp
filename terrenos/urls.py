from django.conf.urls import url, include
from django.urls import path
from .views import *


urlpatterns = [

    url(r"^$", homepage, name='homepage'),

]