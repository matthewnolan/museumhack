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





from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Snippet
from .serializers import SnippetSerializer


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def snippet_list(request, format=None):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


