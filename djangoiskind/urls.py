from django.conf.urls import patterns, include, url
from django.contrib import admin
from test_app.views import hello, current_datetime, hours_ahead, index, order_notice

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoiskind.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    ('^$', index),
    url(r'^admin/', include(admin.site.urls)),
    url('^hello/$', hello),
    ('^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    (r'^my_order/$', order_notice),
)
