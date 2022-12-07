from django.core import serializers
from personal_portfolio.settings import STATIC_DIR
from projects.models import *
import json
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "personal_portfolio.settings")


def retrieve_projects():
    projects_folder = f'{STATIC_DIR}\data\projects'
    if not os.path.exists(projects_folder):
        return []

    for filename in os.listdir(projects_folder):
         if filename.endswith(".json"):
            with open(projects_folder + "\\" + filename, 'r') as json_file:
                my_dict = json.load(json_file)[0]
                print(my_dict)

                #for deserialized in serializers.deserialize("json", my_dict):
                #    print(deserialized)


def retrieve_tech_stacks():
    pass


def retrieve_certifications():
    pass


def retrieve_academic_background():
    pass


def run(option):
    if "photo" in option:
        retrieve_projects()
    
    elif option == "tech":
        retrieve_tech_stacks()
    
    elif "certificate" in option:
        retrieve_certifications()
    
    elif option.lower() in ["academic", "academia"]:
        retrieve_academic_background()

    elif option == "all":
        retrieve_projects()
        retrieve_tech_stacks()
        retrieve_certifications()
        retrieve_academic_background()