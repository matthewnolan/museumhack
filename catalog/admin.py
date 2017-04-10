from django.contrib import admin

# Register your models here.
from .models import Person, Donation, Donorgroup, Institution


# admin.site.register(Donation)
# admin.site.register(Donorgroup)
# admin.site.register(Institution)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('person_name', 'company', 'linkedin')
    fields = ['person_name', 'company', 'linkedin']
admin.site.register(Person, PersonAdmin)


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('person', 'institution', 'donorgroup', 'amount', 'donation_date', 'collection_date', 'data_source_name', 'data_source_url')


@admin.register(Donorgroup)
class DonorgroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
