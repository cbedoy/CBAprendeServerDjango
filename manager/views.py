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


"""
    WEB SERVICES

"""


def user_info(request, _id):
    data = User.objects.get(pk=_id)
    json = serializers.serialize('json', data)
    return HttpResponse(json, mimetype='application/json')


def exam(request, _level):
    data = Question.objects.order_by('?')[:_level]
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


class StatisticList(ListView):
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
