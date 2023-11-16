from grapes.views import *
from django.urls import path
urlpatterns=[
    path("login/",login,name="login")
]