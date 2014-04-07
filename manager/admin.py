__author__ = 'Carlos'

from django.contrib import admin
from .models import *

admin.site.register(question)
admin.site.register(user)
admin.site.register(theme)
admin.site.register(course)
admin.site.register(stadistics)