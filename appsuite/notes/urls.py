from django.conf.urls import patterns, include, url
from notes.views import index, example, dashboard, logmeout
from tastypie.api import Api
from models import NoteResources

v1_api = Api(api_name='v1')
v1_api.register(NoteResources())

urlpatterns = patterns('',
    url(r'^index/', index, name="index"),
    url(r'^example/', example, name="example"),
    url(r'^dashboard/', dashboard, name="dashboard"),
    url(r'^logout/', logmeout, name="logout"),
    url(r'^api/', include(v1_api.urls)),
)
