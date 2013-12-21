from django.conf.urls import patterns, include, url

from notes.views import index, example, dashboard

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'appsuite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^index/', index, name="index"),
    url(r'^example/', example, name="example"),
    url(r'^dashboard/', dashboard, name="dashboard"),
)
