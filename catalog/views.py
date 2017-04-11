from django.shortcuts import render

from .models import Person, Donation, Donorgroup, Institution 
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_donors=Person.objects.all().count()
    num_donations=Donation.objects.all().count()
    num_donorgroups=Donorgroup.objects.all().count()
    num_institutions=Institution.objects.all().count()

    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1


    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
         context={'num_donors':num_donors,'num_donations':num_donations,'num_donorgroups':num_donorgroups,'num_institutions':num_institutions,
            'num_visits':num_visits}, # num_visits appended
    )


class InstitutionListView(generic.ListView):
    model = Institution
    paginate_by = 10

class InstitutionDetailView(generic.DetailView):
    model = Institution

class PersonListView(generic.ListView):
    model = Person

class PersonDetailView(generic.DetailView):
    model = Person

class DonorgroupListView(generic.ListView):
    model = Donorgroup

class DonorgroupDetailView(generic.DetailView):
    model = Donorgroup