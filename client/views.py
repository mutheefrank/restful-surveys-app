# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.edit import FormView
from random import randint
from forms import UserForm
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import *
from forms import *
from django.contrib.auth.models import User
from django.db.models import Count
from django.core import serializers
from django.conf import settings
from rest_framework import viewsets

import json
import os

class Index(TemplateView):
    """
    homepage
    with model summaries
    """

    template_name = 'home.html'


    def getDrinkName(self, id_item):
        return Drink.objects.get(id=str(id_item))

    def getLocationName(self, id_item):
        return Location.objects.get(id=str(id_item))

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data()

        context['survey_locations'] = Location.objects.all()
        context['survey_drinks'] = Drink.objects.all()
        context['surveyors'] = User.objects.all()
        context['survey_respondents'] = DrinkSurvey.objects.all()
        context['count_of_surveys'] = DrinkSurvey.objects.all().count()

        summary_drinks = DrinkSurvey.objects.values('drink').annotate\
            (drink_count=Count('drink')).order_by('-drink_count')

        popular_drinks = []

        for item in summary_drinks:
            drink = self.getDrinkName(item['drink'])
            drink_count = item['drink_count']
            drinks_dict = {'drink':drink, 'drink_count':drink_count}
            popular_drinks.append(drinks_dict)

        context['popular_drinks'] = popular_drinks

        popular_locations = []
        summary_locations = DrinkSurvey.objects.values('research_area').annotate\
            (drink_count=Count('drink')).order_by('-drink_count')


        for item in summary_locations:
            location = self.getLocationName(item['research_area'])
            drink_count = item['drink_count']
            locations_dict = {'location':location, 'drink_count':drink_count}
            popular_locations.append(locations_dict)

        context['popular_locations'] = popular_locations

        all_objects = list(Drink.objects.all()) +\
                      list(DrinkSurvey.objects.all()) +\
                      list(Location.objects.all())


        json_data = serializers.serialize('json', all_objects)
        print json_data

        with open(os.path.join(settings.MEDIA_ROOT,'data.txt'),'w') as f:
            json.dump(json_data, f)

        context['f'] = os.path.join(settings.MEDIA_URL, 'data.txt')
        print context['f']
        return context


class ApiView(TemplateView):
    """
    Api Doc
    """
    template_name = 'api.html'

    def get_context_data(self, **kwargs):
        context = super(ApiView, self).get_context_data()
        return context

class UserFormView(FormView):
    """
    CBS for registering superuser
    """

    template_name = 'signup.html'
    form_class = UserForm

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('/client/login/')

class CrudView(LoginRequiredMixin,TemplateView):
    """
    crud actions landing page
    """
    template_name = 'crud.html'
    def get_context_data(self, **kwargs):
        context = super(CrudView, self).get_context_data()
        return context

class ListLocationsView(LoginRequiredMixin,ListView):
    """
    list all locations cbv
    """
    model = Location
    template_name = 'list_locations.html'
    context_object_name = 'locations'


class AddLocationView(LoginRequiredMixin,CreateView):
    """
    add location cbv
    """
    model = Location
    form_class = LocationForm
    template_name = 'add_locations.html'

    def get_success_url(self):
        return reverse('locations-list')

class DeleteLocationView(LoginRequiredMixin, DeleteView):
    """
    cbv for delete action
    """
    model = Location
    template_name = 'delete_location.html'

    def get_success_url(self):
        return reverse('locations-list')

class UpdateLocationView(LoginRequiredMixin, UpdateView):
    """
    cbv to update location
    """
    model = Location
    template_name = 'update_location.html'
    form_class = LocationForm

    def get_success_url(self):
        return reverse('locations-list')

class ListDrinksView(LoginRequiredMixin, ListView):
    """
    list all drinks
    """
    model = Drink
    template_name = 'list_drinks.html'
    context_object_name = 'drinks'

class AddDrinkView(LoginRequiredMixin, CreateView):
    """
    add drink cbv
    """
    model = Drink
    form_class = DrinkForm
    template_name = 'add_drink.html'

    def get_success_url(self):
        return reverse('drinks-list')

class DeleteDrinkView(LoginRequiredMixin, DeleteView):
    """
    cbv for delete action
    """
    model = Drink
    template_name = 'delete_drink.html'

    def get_success_url(self):
        return reverse('drinks-list')

class UpdateDrinkView(LoginRequiredMixin, UpdateView):
    """
    cbv to update location
    """
    model = Drink
    template_name = 'update_drink.html'
    form_class = DrinkForm

    def get_success_url(self):
        return reverse('drinks-list')


class ListSurveysView(LoginRequiredMixin, ListView):
    """
    list all drink preference surveys
    """
    model = DrinkSurvey
    template_name = 'list_surveys.html'
    context_object_name = 'surveys'

class AddSurveyView(LoginRequiredMixin, CreateView):
    """
    add survey cbv
    """
    model = DrinkSurvey
    form_class = SurveyForm
    template_name = 'add_survey.html'

    def get_success_url(self):
        return reverse('surveys-list')

    def form_valid(self, form):
        form.instance.researcher = self.request.user
        form.instance.research_id = randint(1000,9999)
        form.save()
        return HttpResponseRedirect(self.get_success_url())

class DeleteSurveyView(LoginRequiredMixin,DeleteView):
    """
    delete survey cbv
    """
    model = DrinkSurvey
    template_name = 'delete_survey.html'

    def get_success_url(self):
        return reverse('surveys-list')


class UpdateSurveyView(LoginRequiredMixin, UpdateView):
    """
    update survey cbv
    """
    model = DrinkSurvey
    template_name = 'update_survey.html'
    form_class = SurveyForm


    def get_success_url(self):
        return reverse('surveys-list')

