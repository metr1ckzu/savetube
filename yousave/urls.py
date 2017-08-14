from django.conf.urls import url
from django.contrib import admin
from downloader import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.submit, name='index'),
    url(r'^submit/$', views.submit, name='index'),
]
