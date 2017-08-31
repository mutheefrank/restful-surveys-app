# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Location(models.Model):
    """
    capture various locations
    """
    location = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.location


class Drink(models.Model):
    """
    capture various drinks
    """
    drink = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.drink

class DrinkSurvey(models.Model):
    """
    capture research data for drinks preference
    """

    research_id = models.CharField(max_length=4, unique=True)
    research_person = models.CharField(max_length=100)
    research_area = models.ForeignKey(Location)
    drink = models.ForeignKey(Drink)

    researcher = models.ForeignKey(User)
    added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.research_id















