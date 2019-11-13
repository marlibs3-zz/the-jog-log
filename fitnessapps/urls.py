from django.conf.urls import url

from thejoglog import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^logs/new/$', views.new_log, name='new_log'),
]
