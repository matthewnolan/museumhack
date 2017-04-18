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



from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Snippet
from .serializers import SnippetSerializer

@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
