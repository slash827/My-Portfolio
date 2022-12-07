from django.shortcuts import render
from projects.models import *
from .utils import group_certificates


def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)


def tech_stack(request):
    tech_stacks = TechStack.objects.all()
    context = {
        'tech_stacks': tech_stacks
    }
    return render(request, 'tech_stack.html', context)


def certificates(request):
    certificates = Certificate.objects.all()
    certificates.order_by('institute')
    cert_keys, cert_values = group_certificates(certificates)

    context = {
        'the_range': range(len(cert_keys)),
        'institutes': cert_keys,
        'certificates': cert_values,
    }
    return render(request, 'certificates.html', context)


def certificate_detail(request, name):
    certificate = Certificate.objects.get(name=name)
    context = {
        'certificate': certificate,
    }
    return render(request, 'certificate_detail.html', context)


def academic(request):
    academic = Degree.objects.all()
    context = {
        'academic': academic
    }
    return render(request, 'academic.html', context)