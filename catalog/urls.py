from django.conf.urls import url
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
    url(r'^institution/(?P<pk>\d+)$', views.InstitutionDetailView.as_view(), name='institution-detail'),
    url(r'^uploadcsv/$', views.UploadView.as_view(), name='uploadcsv'),
]