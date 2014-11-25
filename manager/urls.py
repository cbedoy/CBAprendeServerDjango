"""
    DEVELOP BY CARLOS BEDOY
    MOBILE AND WEB DEVELOPER
    carlos.bedoy@gmail.com
"""
from django.conf.urls import url
from manager import views
urlpatterns = [


    url(r'^theme/get/$', 'manager.views.themes'),
    url(r'^user/get/$', 'manager.views.users'),
    url(r'^question/get/$', 'manager.views.questions'),
    url(r'^statistic/get/$', 'manager.views.statistics'),
    url(r'^course/get/$', 'manager.views.courses'),

    url(r'^user/get/'
        r'(?P<username>\w{0,50})/'
        r'(?P<password>\w{0,50})/$', 'manager.views.user_info'),

    url(r'^theme/get/'
        r'(?P<pk>\w{0,50})/$', 'manager.views.theme_from_course'),

    url(r'^user/add/'
        r'(?P<username>\w{0,50})/'
        r'(?P<password>\w{0,50})/'
        r'(?P<firstName>\w{0,50})/'
        r'(?P<lastName>\w{0,50})/'
        r'(?P<facebook>\w{0,50})/'
        r'(?P<twitter>\w{0,50})/'
        r'(?P<age>\w{0,50})$', 'manager.views.user_new'),

    url(r'^user_rank/get', 'manager.views.user_ranks'),

    url(r'^feed_by_user/get/'
        r'(?P<player_key>\w{0,50})/$', 'manager.views.feed_by_user'),

    url(r'^exam/get/'
        r'(?P<theme>\w{0,50})/'
        r'(?P<level>\w{0,50})/', 'manager.views.exam_theme_level'),

    url(r'^random_exam/get/'
        r'(?P<level>\w{0,50})/', 'manager.views.exam_random'),

    url(r'^user_rank/get', 'manager.views.user_ranks'),

    url(r'^feed/new/'
        r'(?P<level>\w{0,50})/'
        r'(?P<correct>\w{0,50})/'
        r'(?P<wrongs>\w{0,50})/'
        r'(?P<points>\w{0,50})/'
        r'(?P<course>\w{0,50})/'
        r'(?P<theme>\w{0,50})/'
        r'(?P<player>\w{0,50})/$', 'manager.views.feed_new'),


    url(r'^theme/new', views.ThemeCreate.as_view(), name='theme_new'),
    url(r'^user/new', views.UserCreate.as_view(), name='user_new'),
    url(r'^question/new', views.QuestionCreate.as_view(), name='question_new'),
    url(r'^course/new', views.CourseCreate.as_view(), name='course_new'),

    url(r'^theme/delete/(?P<pk>\d+)$', views.ThemeDelete.as_view(), name='theme_delete'),
    url(r'^course/delete/(?P<pk>\d+)$', views.CourseDelete.as_view(), name='course_delete'),
    url(r'^question/delete/(?P<pk>\d+)$', views.QuestionDelete.as_view(), name='question_delete'),

    url(r'^theme/edit/(?P<pk>\d+)$', views.ThemeEdit.as_view(), name='theme_edit'),
    url(r'^course/edit/(?P<pk>\d+)$', views.CourseEdit.as_view(), name='course_edit'),
    url(r'^question/edit/(?P<pk>\d+)$', views.QuestionEdit.as_view(), name='question_edit'),
    url(r'^user/edit/(?P<pk>\d+)$', views.UserEdit.as_view(), name='user_edit'),

    url(r'^theme/list', views.ThemeList.as_view(), name='theme_list'),
    url(r'^user/list', views.UserList.as_view(), name='user_list'),
    url(r'^question/list', views.QuestionList.as_view(), name='question_list'),
    url(r'^statistic/list', views.StatisticsList.as_view(), name='statistics_list'),
    url(r'^course/list', views.CourseList.as_view(), name='course_list'),

]