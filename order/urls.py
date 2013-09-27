from django.conf.urls import patterns, include, url
import settings
from order.function import WebHome, rest

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^WebHome/$', WebHome),
    (r'^rest/(\d+)/$', rest),
    # Examples:
    # url(r'^$', 'order.views.home', name='home'),
    # url(r'^order/', include('order.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
