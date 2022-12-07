from django.core import serializers
from personal_portfolio.settings import STATIC_DIR
from projects.models import *
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "personal_portfolio.settings")


def projects_to_json():
    projects = Project.objects.all()
    
    for project in projects:
        serialized_obj = serializers.serialize('json', [ project, ])

        projects_folder = f'{STATIC_DIR}\data\projects'
        if not os.path.exists(projects_folder):
            os.makedirs(projects_folder)

        with open(projects_folder + rf'\{project.title}.json', 'w') as json_file:
            json_file.write(serialized_obj)


def tech_stacks_to_json():
    tech_stacks = TechStack.objects.all()
    
    for tech_stack in tech_stacks:
        serialized_obj = serializers.serialize('json', [ tech_stack, ])

        tech_stacks_folder = rf"{STATIC_DIR}\data\tech_stacks"
        if not os.path.exists(tech_stacks_folder):
            os.makedirs(tech_stacks_folder)

        with open(tech_stacks_folder + f'\{tech_stack.name}.json', 'w') as json_file:
            json_file.write(serialized_obj)


def certificates_to_json():
    certificates = Certificate.objects.all()
    
    for certificate in certificates:
        serialized_obj = serializers.serialize('json', [ certificate, ])

        certificate_folder = rf'{STATIC_DIR}\data\certificates\{certificate.institute}'
        if not os.path.exists(certificate_folder):
            os.makedirs(certificate_folder)

        with open(certificate_folder + f'\{certificate.name}.json', 'w') as json_file:
            json_file.write(serialized_obj)


def degrees_to_json():
    degrees = Degree.objects.all()
    
    for degree in degrees:
        serialized_obj = serializers.serialize('json', [ degree, ])

        degrees_folder = rf'{STATIC_DIR}\data\degrees'
        if not os.path.exists(degrees_folder):
            os.makedirs(degrees_folder)

        with open(degrees_folder + f'\{degree.title}.json', 'w') as json_file:
            json_file.write(serialized_obj)


def run():
    projects_to_json()
    tech_stacks_to_json()
    certificates_to_json()
    degrees_to_json()
