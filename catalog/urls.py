from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'), 
]

urlpatterns += [
    url(r'^persons/$', views.PersonListView.as_view(), name='persons'),
    url(r'^person/(?P<pk>\d+)$', views.PersonDetailView.as_view(), name='person-detail'),    
    
    url(r'^donorgroups/$', views.DonorgroupListView.as_view(), name='donorgroups'),
    url(r'^donorgroup/(?P<pk>\d+)$', views.DonorgroupDetailView.as_view(), name='donorgroup-detail'), 
       
    url(r'^institutions/$', views.InstitutionListView.as_view(), name='institutions'),
    url(r'^institution/(?P<slug>[-\w]+)/$', views.InstitutionDetailView, name='institution-detail'),
    url(r'^institution/(?P<slug>[-\w]+)/donors/$', views.InstitutionPersonListView, name='institution-donors'),
]

## TODO do I need this?
# from rest_framework.urlpatterns import format_suffix_patterns
# urlpatterns = format_suffix_patterns(urlpatterns)
