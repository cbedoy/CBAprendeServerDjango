"""
    DEVELOP BY CARLOS BEDOY
    MOBILE AND WEB DEVELOPER
    carlos.bedoy@gmail.com
"""
from django.conf.urls import url

urlpatterns = [


    url(r'^themes/get/$', 'manager.views.themes'),
    url(r'^users/get/$', 'manager.views.users'),
    url(r'^question/get/$', 'manager.views.question'),
    url(r'^statistics/get/$', 'manager.views.statistics'),
    url(r'^courses/get/$', 'manager.views.courses'),

]