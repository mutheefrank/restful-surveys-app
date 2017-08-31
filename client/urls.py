from django.conf.urls import url
from django.contrib.auth import views
from views import *


urlpatterns = [

    url(r'^$', Index.as_view(), name='index'),

    url(r'^client/login/$', views.login, {'template_name':'login.html'}, name='login'),

    url(r'^client/logout/$', views.logout,{'template_name':'logout.html'}, name='logout'),

    url(r'^client/signup/$', UserFormView.as_view(), name='signup'),

    url(r'^client/api/$', ApiView.as_view(), name='api'),

    url(r'^client/crud/$', CrudView.as_view(), name='crud'),

    url(r'^client/crud/locations/$', ListLocationsView.as_view(), name='locations-list'),

    url(r'^client/crud/locations/add/$', AddLocationView.as_view(), name='locations-add'),

    url(r'^client/crud/locations/delete/(?P<pk>\d+)/$', DeleteLocationView.as_view(), name='locations-delete'),

    url(r'^client/crud/locations/update/(?P<pk>\d+)/$', UpdateLocationView.as_view(), name='locations-update'),

    url(r'^client/crud/drinks/$', ListDrinksView.as_view(), name='drinks-list'),

    url(r'^client/crud/drinks/add/$', AddDrinkView.as_view(), name='drinks-add'),

    url(r'^client/crud/drinks/delete/(?P<pk>\d+)/$', DeleteDrinkView.as_view(), name='drinks-delete'),

    url(r'^client/crud/drinks/update/(?P<pk>\d+)/$', UpdateDrinkView.as_view(), name='drinks-update'),

    url(r'^client/crud/surveys/$', ListSurveysView.as_view(), name='surveys-list'),

    url(r'^client/crud/surveys/add/$', AddSurveyView.as_view(), name='survey-add'),

    url(r'^client/crud/surveys/delete/(?P<pk>\d+)/$', DeleteSurveyView.as_view(), name='survey-delete'),

    url(r'^client/crud/surveys/update/(?P<pk>\d+)/$', UpdateSurveyView.as_view(), name='survey-update'),

]
