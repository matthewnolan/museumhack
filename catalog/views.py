from django.shortcuts import render
from .models import Person, Donation, Donorgroup, Institution 
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.db.models import Count, Min, Max, Sum, Avg

def index(request):
    # Generate counts of some of the main objects
    num_donors=Person.objects.all().count()
    num_donations=Donation.objects.all().count()
    num_donorgroups=Donorgroup.objects.all().count()
    num_institutions=Institution.objects.all().count()

    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    return render(
        request,
        'index.html',
         context={'num_donors':num_donors,'num_donations':num_donations,'num_donorgroups':num_donorgroups,'num_institutions':num_institutions,
            'num_visits':num_visits}, 
    )


class InstitutionListView(generic.ListView):
    model = Institution
    paginate_by = 30
    def get_context_data(self, **kwargs):
        context = super(InstitutionListView, self).get_context_data(**kwargs)
        context['num_institutions'] = Institution.objects.all().count()
        return context      


def InstitutionDetailView(request, slug):
    this_institution = Institution.objects.get(slug=slug)
    institution_donors = Person.objects.filter(donation__institution=this_institution).annotate(num_donations=Count('donation')).order_by('-num_donations')[:6]
    institution_donor_lists = Donation.objects.filter(institution=this_institution).order_by('donation_list').distinct('donation_list')
    institution_donorgroups = Donorgroup.objects.filter(institution=this_institution).order_by('name')

    return render(
        request,
        'catalog/institution_detail.html',
         context={'institution':this_institution, 
         'institution_donors': institution_donors,
         'institution_donor_lists': institution_donor_lists,
         'institution_donorgroups': institution_donorgroups}, 
    )


def InstitutionPersonListView(request, slug):
    this_institution = Institution.objects.get(slug=slug)
    institution_donors = Person.objects.filter(donation__institution=this_institution).annotate(num_donations=Count('donation')).order_by('-num_donations')

    return render(
        request,
        'catalog/institution_donors.html',
         context={'institution':this_institution, 
         'institution_donors': institution_donors}, 
    )


class PersonListView(generic.ListView):
    paginate_by = 50
    model = Person
    def get_queryset(self):
        # pass this to the url ?orderby=-name    or  num_donations
        order = self.request.GET.get('orderby', '-num_donations')
        new_context = Person.objects.annotate(num_donations=Count('donation')).order_by(order)
        return new_context

    def get_context_data(self, **kwargs):
        context = super(PersonListView, self).get_context_data(**kwargs)
        context['num_donors'] = Person.objects.all().count()
        context['orderby'] = self.request.GET.get('orderby', 'name')
        return context    


class PersonDetailView(generic.DetailView):
    model = Person


class DonorgroupListView(generic.ListView):
    model = Donorgroup
    def get_context_data(self, **kwargs):
        context = super(DonorgroupListView, self).get_context_data(**kwargs)
        context['num_donorgroups'] = Donorgroup.objects.all().count()
        return context      


class DonorgroupDetailView(generic.DetailView):
    model = Donorgroup
    paginate_by = 30   
    # queryset = Donorgroup.objects.order_by('donation__person')
