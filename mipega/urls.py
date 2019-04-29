from django.conf.urls import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mipega.views.home', name='home'),
    # url(r'^mipega/', include('mipega.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('MP.urls')),
	url('^', include('django.contrib.auth.urls')),
    url(r'^reset/password_reset$', password_reset, {'template_name':'registration/password_reset_form.html', 'email_template_name': 'registration/password_reset_email.html'}, name='password_reset'),
    url(r'^reset/password_reset_done$', password_reset_done, {'template_name': 'registration/password_reset_done.html'}, name = "password_reset_done"),
)
