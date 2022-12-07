from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("projects/<int:pk>/", views.project_detail, name="project_detail"),
    path("tech-stack", views.tech_stack, name="tech_stack"),
    path("certificates", views.certificates, name="certificates"),
    path("certificate/<str:name>", views.certificate_detail, name="certificate_detail"),
    path("academic", views.academic, name="academic"),
]