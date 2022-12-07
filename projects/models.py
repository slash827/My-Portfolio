from django.db import models
from django.contrib.postgres.fields import ArrayField


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    technology = models.CharField(max_length=50)
    image = models.FilePathField(path="/img")


class TechStack(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    extra = models.TextField(default=None, blank=True, null=True)


class Certificate(models.Model):
    institute = models.CharField(max_length=100)
    name = models.CharField(max_length=100, default=None, blank=True, null=True)
    link = models.CharField(max_length=256, default=None, blank=True, null=True)


class Degree(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    courses_names = ArrayField(models.CharField(max_length=100))
    