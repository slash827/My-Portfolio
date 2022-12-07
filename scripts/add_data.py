from projects.models import *
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "personal_portfolio.settings")


def add_projects():
    projects = Project.objects.all()
    projects.delete()
    
    title = "Messenger App"
    description = "Messenger App - Client Server application with Python and C++. \
\nA client software that sends encrypted messages between clients on different computers using a model of client-server. \
\nThe client side is written in C++ and has a Command line interface. \
\nThe server side is written in Python and uses socket for network communication."
    technology = "Python and C++"
    image = "img/messenger_app.png"

    projects.create(title=title, description=description, technology=technology, image=image)


    title = "Genetic Algorithm With The Game Of Life"
    description = "Using genetic algorithms to explore the game of life. \
    \nThis project was built with python and implements a genetic algorithm that finds patterns in the game of life that are called \
    methuselahs. \nThis project was a final project in a course about Computational Biology."
    technology = "Python with Numpy"
    image = "img/genetic_project.png"

    projects.create(title=title, description=description, technology=technology, image=image)
    
  
    title = "Automating Anomaly Detection"
    description = "Extension to MetaOD software - an Outlier Detection automation tool. \
\nAnomaly Detection automation tool, used to help with the model-selection problem in case of Anomaly detection Machine Learning \
models, and automating the process."
    technology = "Python with ML libraries"
    image = "img/autoAD.png"

    projects.create(title=title, description=description, technology=technology, image=image)


def add_tech_stacks():
    tech_stacks = TechStack.objects.all()
    tech_stacks.delete()

    name = "Python"
    description = "Advanced Python including OOP, Meta Programming, Network and Socket programming and Excepion Handelling."
    extra = "Libraries like: Pandas, NumPy, Matplotlib, Sklearn, TensorFlow, Django."
    tech_stacks.create(name=name, description=description, extra=extra)

    name = "Java"
    description = "OOP, Java Collections and Generic types, Threads and Excepion Handelling." 
    tech_stacks.create(name=name, description=description, extra="")


    name = "C++"
    description = "OOP, Network and Socket programming."
    tech_stacks.create(name=name, description=description, extra="")


    name = "HTML CSS and JavaScript"
    description = "Basic tags, Styles and JavaScript operations - currently learning in self-pace."
    tech_stacks.create(name=name, description=description)


def add_certifications():
    certificates = Certificate.objects.all()
    certificates.delete()
    
    institute = "freeCodeCamp"
    names = [ "Scientific Computing with Python",
        "Data Analysis with Python",
        "JavaScript Algorithms and Data Structures",
    ]
    links = [ "https://www.freecodecamp.org/certification/fcccda59c64/scientific-computing-with-python-v7",
        "https://www.freecodecamp.org/certification/fcccda59c64/data-analysis-with-python-v7",
        "https://www.freecodecamp.org/certification/fcccda59c64/javascript-algorithms-and-data-structures",
    ]
    for i, _ in enumerate(names):
        certificates.create(institute=institute, name=names[i], link=links[i])

    institute = "Udemy"
    names = [ "Automate the Boring Stuff with Python Programming",
        "Practical Machine Learning by Example in Python"]

    IMAGES_PATH = "data/pdf/"
    links = [IMAGES_PATH + names[i].replace(' ', '_') + ".png" for i in range(len(names))]

    for i, _ in enumerate(names):
        certificates.create(institute=institute, name=names[i], link=links[i])


def add_academic_background():
    degrees = Degree.objects.all()
    degrees.delete()
    
    title = "Bachelor Degree"
    description = "Computer Science from The Open University of Israel, GPA 90."
    courses_names = [ "Data Structures and Algorithms",
        "Database Management Systems - with PostgreSQL",
        "Computational Biology",
        "Intro to Artificial Intelligence",
        "Seminar in Cybersecurity with Machine Learning",
        "Defensive System Programming",
    ]
    degrees.create(title=title, description=description, courses_names=courses_names)

    title = "Master Degree"
    description = "Studying Computer Science with thesis in AI at Bar-Ilan University."
    courses_names = [ "Image Processing",
        "Machine Learning",
        "Tabular Data Science",
        "Data Science Workshop",
    ]
    degrees.create(title=title, description=description, courses_names=courses_names)


def run(option):
    if "photo" in option:
        add_projects()
    
    elif option == "tech":
        add_tech_stacks()
    
    elif "certificate" in option:
        add_certifications()
    
    elif option.lower() in ["academic", "academia"]:
        add_academic_background()
    
    elif option == "all":
        add_projects()
        add_tech_stacks()
        add_certifications()
        add_academic_background()