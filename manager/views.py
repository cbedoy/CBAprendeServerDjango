"""
    DEVELOP BY CARLOS BEDOY
    MOBILE AND WEB DEVELOPER
    carlos.bedoy@gmail.com
"""
from django.http import HttpResponse

from models import *
from django.core import serializers


def themes(request):
    data = Theme.objects.all()
    json = serializers.serialize('json', data)
    return HttpResponse(json, mimetype='application/json')


def courses(request):
    data = Course.objects.all()
    json = serializers.serialize('json', data)
    return HttpResponse(json, mimetype='application/json')


def users(request):
    data = User.objects.all()
    json = serializers.serialize('json', data)
    return HttpResponse(json, mimetype='application/json')


def statistics(request):
    data = Statistics.objects.all()
    json = serializers.serialize('json', data)
    return HttpResponse(json, mimetype='application/json')


def questions(request):
    data = Question.objects.all()
    json = serializers.serialize('json', data)
    return HttpResponse(json, mimetype='application/json')


