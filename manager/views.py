"""
    DEVELOP BY CARLOS BEDOY
    MOBILE AND WEB DEVELOPER
    carlos.bedoy@gmail.com
"""
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.db import connection
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from .models import *
from django.http import HttpResponse
from django.core import serializers
import datetime


def themes(request):
    data = Theme.objects.select_related().order_by('course')
    json = serializers.serialize('json', data)
    return HttpResponse(json, mimetype='application/json')


def courses(request):
    data = Course.objects.all()
    json = serializers.serialize('json', data)
    return HttpResponse(json, mimetype='application/json')


def university(request):
    data = University.objects.all()
    json = serializers.serialize('json', data)
    return HttpResponse(json, mimetype='application/json')


def users(request):
    data = User.objects.all().order_by('-points')
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


"""
    WEB SERVICES

"""


def feed_new(request, level, correct, wrongs, points, player):
    data = Statistics(level=level, correct=correct, wrongs=wrongs,
                      points=points, date=datetime.date.now(), player=player)
    data.save()
    json = serializers.serialize('json', data, indent=4)
    return HttpResponse(json, mimetype='application/json')


def user_info(request, username, password):
    data = User.objects.filter(username=username, password=password)

    json = serializers.serialize('json', data, indent=4)
    return HttpResponse(json, mimetype='application/json')


def user_new(request, username, password, firstName, lastName, university, facebook, twitter, age):
    data = User(username=username, password=password, firstName=firstName, lastName=lastName,
                university=university, facebook=facebook, twitter=twitter, age=age)
    data.save()
    json = serializers.serialize('json', data, indent=4)
    return HttpResponse(json, mimetype='application/json')


def exam_theme_level(request, theme, level):
    data = Question.objects.filter(theme=theme).order_by('?')[:level]
    json = serializers.serialize('json', data)
    return HttpResponse(json, mimetype='application/json')


def exam_random(request, level):
    data = Question.objects.order_by('?')[:level]
    json = serializers.serialize('json', data)
    return HttpResponse(json, mimetype='application/json')


def user_ranks(request):
    data = User.objects.order_by('points')
    json = serializers.serialize('json', data)
    return HttpResponse(json, mimetype='application/json')

"""

        WEP APP <3

"""


class QuestionList(ListView):
    model = Question


class UserList(ListView):
    model = User


class ThemeList(ListView):
    model = Theme


class CourseList(ListView):
    model = Course


class StatisticsList(ListView):
    model = Statistics


class QuestionCreate(CreateView):
    model = Question


class UserCreate(CreateView):
    model = User


class CourseCreate(CreateView):
    model = Course


class ThemeCreate(CreateView):
    model = Theme


class QuestionEdit(UpdateView):
    model = Question


class UserEdit(UpdateView):
    model = User


class ThemeEdit(UpdateView):
    model = Theme


class CourseEdit(UpdateView):
    model = Course


class QuestionDelete(DeleteView):
    model = Question


class CourseDelete(DeleteView):
    model = Course


class ThemeDelete(DeleteView):
    model = Theme
