# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from models import *

from django.contrib import admin

# Register your models here.

class LocationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Location, LocationAdmin)


class ResearchAdmin(admin.ModelAdmin):
    pass