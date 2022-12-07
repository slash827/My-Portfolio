from django.urls import path
from . import views

urlpatterns = [
    path("contact", views.contact, name="contact_me"),
    path("about", views.about_me, name="about_me"),
]