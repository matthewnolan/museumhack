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
    url(r'^institution/(?P<pk>\d+)$', views.InstitutionDetailView.as_view(), name='institution-detail'),

    url(r'^uploadcsv/$', views.UploadView.as_view(), name='uploadcsv'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]






# http://www.django-rest-framework.org/tutorial/2-requests-and-responses/

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns += [
    # url(r'^', include(router.urls)),
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]

