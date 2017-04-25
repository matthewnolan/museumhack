from django.shortcuts import render
from .models import Person, Donation, Donorgroup, Institution 
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.db.models import Count, Min, Sum, Avg
# from django.contrib.auth.decorators import permission_required


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
            'num_visits':num_visits}, # num_visits appended
    )


class InstitutionListView(generic.ListView):
    model = Institution
    paginate_by = 30
    def get_context_data(self, **kwargs):
        context = super(InstitutionListView, self).get_context_data(**kwargs)
        context['num_institutions'] = Institution.objects.all().count()
        return context      

# class InstitutionDetailView(generic.DetailView):
#     model = Institution

from django.db.models import Count, Max, Min

def InstitutionDetailView(request, pk):

    this_institution = Institution.objects.get(pk=pk)
    institution_donors = Person.objects.filter(donation__institution=this_institution).annotate(num_donations=Count('donation')).order_by('-num_donations')[:5]
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

# TODO cleanup
class PersonListView(generic.ListView):
    paginate_by = 90
    # model = Person
    # buggy. produces duplicates
    # queryset = Person.objects.order_by('-donation__donation_date_start')
    queryset = Person.objects.order_by('name')
    def get_context_data(self, **kwargs):
        context = super(PersonListView, self).get_context_data(**kwargs)
        context['num_donors'] = Person.objects.all().count()
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



# TODO remove this
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class InstitutionCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('catalog.is_staff')

    model = Institution
    fields = '__all__'
    initial={'location':'Detroit',}

class InstitutionUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('catalog.is_staff')

    model = Institution
    fields = ['name','city']

class InstitutionDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('catalog.is_staff')

    model = Institution
    success_url = reverse_lazy('institutions')



# TODO use API or remove it
# from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework import generics
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly


class SnippetList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
    queryset = Institution.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
    queryset = Institution.objects.all()
    serializer_class = SnippetSerializer



from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import csv
from itertools import islice
import codecs

class CsvLoad(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
    
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # csvOut = csv.reader(request.data, delimiter=',')
        # for line in islice(csvOut, 1, None):
        #     print("ok")
        # print("")
        # print(request.data)
        # print("")



        # reader = csv.reader(request.data)
        # for row in reader:            
        #     print("ok")


        # csvfile = request.FILES['csv_file']
        # dialect = csv.Sniffer().sniff(codecs.EncodedFile(csvfile, "utf-8").read(1024))
        # # print(dialect)
        # csvfile.open()
        # reader = csv.reader(codecs.EncodedFile(csvfile, "utf-8"), delimiter=',', dialect=dialect)
        # print(reader)


        # file = request.FILES['fileUpload']
        # data = [row for row in csv.reader(file)]



        return Response("its good", status=status.HTTP_201_CREATED)

        # serializer = SnippetSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



