from rest_framework import routers
from views import DrinkSurveyViewSet, DrinkViewSet, LocationViewSet
from views import login
from django.conf.urls import url, include

router = routers.DefaultRouter()
router.register(r'drinks', DrinkViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'surveys', DrinkSurveyViewSet)



urlpatterns = [
    url(r'^login', login),
]

urlpatterns += router.urls