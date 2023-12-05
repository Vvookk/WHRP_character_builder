from django.urls import path
from whrp_site import views

urlpatterns = [
    path("", views.home, name="home"),
]
