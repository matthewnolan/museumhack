from django.conf.urls import url, include
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    # url(r'^$', views.index, name='index'), 
]

urlpatterns += [
    url(r'^persons/$', views.PersonListView.as_view(), name='persons'),
    url(r'^person/(?P<pk>\d+)$', views.PersonDetailView.as_view(), name='person-detail'),    
    
    url(r'^donorgroups/$', views.DonorgroupListView.as_view(), name='donorgroups'),
    url(r'^donorgroup/(?P<pk>\d+)$', views.DonorgroupDetailView.as_view(), name='donorgroup-detail'), 
       
    url(r'^institutions/$', views.InstitutionListView.as_view(), name='institutions'),
    url(r'^institution/(?P<slug>[-\w]+)/$', views.InstitutionDetailView, name='institution-detail'),
    url(r'^institution/(?P<slug>[-\w]+)/donors/$', views.InstitutionPersonListView, name='institution-donors'),

    # TODO remove this when we want to use the index
    url(r'^.*$', RedirectView.as_view(url='institution/the-metropolitan-museum-of-art/', permanent=False), name='index')
]