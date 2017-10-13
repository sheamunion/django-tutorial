from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    # e.g. /polls/
    # url(r'^$', views.index, name='index'),
    # Use generic views instead:
    url(r'^$', views.IndexView.as_view(), name='index'),
    # e.g. /polls/5/
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # e.g. /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # e.g. /polls/5/vote
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
