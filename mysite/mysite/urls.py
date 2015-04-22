from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'home.views.index', name='home'),
    url(r'^Finances/$', 'Finances.views.index', name='Finances'),
    url(r'^admin/', include(admin.site.urls)),
]
