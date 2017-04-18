from django.contrib import admin
from .models import Person, Donation, Donorgroup, Institution, Snippet

# import export is useful for backup
from import_export import resources, fields
from import_export.resources import ModelResource
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget

class DonationResource(resources.ModelResource):
    # Use fields.Field to export to Foreign key (persons name instead of user id), but gives errors when importing
    # TODO cleanup. remove this.
    # person = fields.Field(
    #     column_name='person',
    #     attribute='person',
    #     widget=ForeignKeyWidget(Person, 'name')
    #     )
    # institution = fields.Field(
    #     column_name='institution',
    #     attribute='institution',
    #     widget=ForeignKeyWidget(Institution, 'name'))
    # donorgroup = fields.Field(
    #     column_name='donorgroup',
    #     attribute='donorgroup',
    #     widget=ForeignKeyWidget(Donorgroup, 'name'))

    class Meta:
        model = Donation
        # fields = ('id','person','donation_full_name','donation_class','event_name','institution','donorgroup','donation_type','amount_exact','amount_range_low','amount_range_high','amount_other','donation_date_start','donation_date_end','collection_date','data_source_name','data_source_url')        

class DonationAdmin(ImportExportModelAdmin):
    resource_class = DonationResource

admin.site.register(Person)
admin.site.register(Donation, DonationAdmin)
admin.site.register(Donorgroup)
admin.site.register(Institution)

# TODO remove. From API test
admin.site.register(Snippet)