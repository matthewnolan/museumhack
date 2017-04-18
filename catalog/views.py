from django.shortcuts import render
from .models import Person, Donation, Donorgroup, Institution 
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
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

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
         context={'num_donors':num_donors,'num_donations':num_donations,'num_donorgroups':num_donorgroups,'num_institutions':num_institutions,
            'num_visits':num_visits}, # num_visits appended
    )


class InstitutionListView(generic.ListView):
    model = Institution
    paginate_by = 30   

class InstitutionDetailView(generic.DetailView):
    model = Institution

# TODO cleanup
# why cant i do this order_by('donation.first.donation_date_start')   !?!?
class PersonListView(generic.ListView):
    model = Person
    # print(model.get_most_recent_donation)
    # ordering = 'model.get_most_recent_donation'
    paginate_by = 30 

# def PersonListView(request): 
#     person_list = Person.objects.all().order_by('donation').limit_by()
#     return render(request, 'catalog/person_list.html', context={'person_list':person_list}) 


class PersonDetailView(generic.DetailView):
    model = Person

class DonorgroupListView(generic.ListView):
    model = Donorgroup
    paginate_by = 30   

class DonorgroupDetailView(generic.DetailView):
    model = Donorgroup


class UploadView(LoginRequiredMixin, generic.ListView):
    model = Donation
    template_name ='catalog/upload_csv.html'






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




from .models import Snippet
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



