from django.contrib import admin
from .models import Person, Donation, Donorgroup, Institution


admin.site.register(Person)
admin.site.register(Donation)
admin.site.register(Donorgroup)
admin.site.register(Institution)
