"""
    DEVELOP BY CARLOS BEDOY
    MOBILE AND WEB DEVELOPER
    carlos.bedoy@gmail.com
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ApprendeServer.views.home', name='home'),
    # url(r'^ApprendeServer/', include('ApprendeServer.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^apprende/', include('manager.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
