from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^feed/(.*)$', "cms_users_put.views.twitter"),
    url(r'^logout$', "django.contrib.auth.views.logout"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', "cms_users_put.views.todo"),
    url(r'^(.*)$', "cms_users_put.views.mostrar"),
)
