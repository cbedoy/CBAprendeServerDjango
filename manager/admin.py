"""
    DEVELOP BY CARLOS BEDOY
    MOBILE AND WEB DEVELOPER
    carlos.bedoy@gmail.com
"""

from django.contrib import admin
from .models import *

admin.site.register(Question)
admin.site.register(User)
admin.site.register(Theme)
admin.site.register(Course)
admin.site.register(Statistics)
admin.site.register(University)