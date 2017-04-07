from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, Person, Donation, Donorgroup, Institution


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








# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

# Register the Admin classes for Book using the decorator

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    

# Register the Admin classes for BookInstance using the decorator

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    
    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower',)
        }),
    )