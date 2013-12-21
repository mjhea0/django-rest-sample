from django.conf.urls import patterns, include, url

from notes.views import index, example, dashboard, logmeout

urlpatterns = patterns('',
    url(r'^index/', index, name="index"),
    url(r'^example/', example, name="example"),
    url(r'^dashboard/', dashboard, name="dashboard"),
    url(r'^logout/', logmeout, name="logout"),
)
