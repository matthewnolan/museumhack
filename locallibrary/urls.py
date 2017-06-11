"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
# Use include() to add URLS from the catalog application 
from django.conf.urls import include
#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView
# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

# Begin Sitemap 
# TODO Clean this Sitemap area
# Make sure a url is set /admin/sites/site/
from django.contrib.sites.models import Site
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from catalog.models import Person, Institution, Donorgroup
from catalog.sitemaps import StaticViewSitemap
person_dict = {
    'queryset': Person.objects.all(),
}
institution_dict = {
    'queryset': Institution.objects.all(),
}
donorgroups_dict = {
    'queryset': Donorgroup.objects.all(),
}
sitemaps = { 
    'person': GenericSitemap(person_dict, priority=0.5),
    'institution': GenericSitemap(institution_dict, priority=0.5),
    'donorgroups': GenericSitemap(donorgroups_dict, priority=0.5),
    'static': StaticViewSitemap
}
# End Sitemap

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('catalog.urls')),
    url(r'^$', RedirectView.as_view(url='/c/', permanent=True)),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^robots.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /admin", content_type='text/plain')),
]

urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    url('^accounts/', include('django.contrib.auth.urls')),
]
