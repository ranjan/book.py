from demoapp.views import current_datetime
from demoapp.views import hello
from demoapp.views import hours_ahead
from django.conf.urls.defaults import *
from django.template import Context
from django.template import Template
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from demoapp.books import views
from demoapp.contact import views as abc

#urlpatterns = patterns('',
  # Example:
  # (r'^demoapp/', include('demoapp.foo.urls')),

  # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
  # to INSTALLED_APPS to enable admin documentation:
  # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

  # Uncomment the next line to enable the admin:
  # (r'^admin/(.*)', admin.site.root),
#)

urlpatterns = patterns('',
  ('^hello/$', hello),
  ('^time/$', current_datetime),
  (r'^time/plus/(\d{1,2})/$', hours_ahead),
  (r'^admin/(.*)', admin.site.root),
  (r'^search/$', views.search),
  (r'^contact/$', abc.contact),
  (r'^contact/thanks/$', abc.thanks),
)