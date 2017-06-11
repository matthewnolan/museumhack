from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse 
from django.utils import timezone
import uuid 

# Get around encoding problems
# https://stackoverflow.com/questions/17974412/django-ascii-codec-cant-encode-character
from django.utils.encoding import python_2_unicode_compatible

# TODO remove this
# from django_autoslug.fields import AutoSlugField
# from django.utils.text import slugify


@python_2_unicode_compatible
class Person(models.Model):
    name = models.CharField(max_length=300)

    def get_most_recent_donation(self):
        donation_date_start = self.donation_set.all().order_by('-donation_date_start').first().donation_date_start
        institution_name = self.donation_set.all().order_by('-donation_date_start').first().institution
        return '%s, %s ' % (donation_date_start.year, institution_name)

    def get_num_donation(self):
        return self.donation_set.all().count()

    def get_absolute_url(self):
        return reverse('person-detail', args=[str(self.id)])

    def __str__(self):
        return '%s' % (self.name)


@python_2_unicode_compatible
class Donation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular donation")

    # Replace Admin Site Foreign Key Field/Dropdown with Textbox?
    # https://groups.google.com/forum/#!topic/django-users/zjdbX5ipRqY
    person = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True) 

    # bill and melinda gates gift for the arts
    donation_full_name = models.CharField(max_length=500, null=True, blank=True)

    # Apollo Circle Chairs
    donation_class = models.CharField(max_length=500, null=True, blank=True)

    # Apollo Circle Benefit 2013
    event_name = models.CharField(max_length=500, null=True, blank=True)

    # The Metropolitan Museum of Art
    institution = models.ForeignKey('Institution', on_delete=models.SET_NULL, null=True) 

    # Apollo Circle 2013
    # There will be many groups with the name Apollo Circle who each have a year associated w each group
    donorgroup = models.ForeignKey('Donorgroup', on_delete=models.SET_NULL, null=True) 

    DONATION_TYPES = (
        ('e', 'Exact Value: $100'),
        ('r', 'Range: $100-$200'),
        ('p', 'Range: $100 and above'),
        ('o', 'Just other'),
        ('u', 'Unknown'),
    )

    donation_type = models.CharField(max_length=1, choices=DONATION_TYPES, default='u', null=True, blank=True, help_text='Donation Type')

    amount_exact = models.DecimalField(max_digits=99, decimal_places=2, null=True, blank=True, help_text="For exact values ie: $100")

    amount_range_low = models.DecimalField(max_digits=99, decimal_places=2, null=True, blank=True, help_text="For range low end ie: $100-$200 or for low end of range ie: $100 and above")

    amount_range_high = models.DecimalField(max_digits=99, decimal_places=2, null=True, blank=True, help_text="For high end $100-$200")

    # Range of amount of money ie  "$500+" or "$1000 to $2000"
    amount_other = models.CharField(max_length=500, null=True, blank=True, help_text="ie: Plus a special gift from our family")

    # Date person donates
    donation_date_start = models.DateField(default=date.today)

    # Date person donates. Some dates are a range
    donation_date_end = models.DateField(null=True, blank=True)

    # Date at which I collected data
    collection_date = models.DateField(null=True, blank=True)

    date_entered = models.DateTimeField(default=timezone.now, help_text="Date entered into this database")

    data_source_name = models.CharField(max_length=500, null=True, blank=True) 

    data_source_url = models.CharField(max_length=500, null=True, blank=True)  
    
    # The name of the spreadsheet from which we import the data. For internal use only. We wont show this data to users.
    donation_list = models.CharField(max_length=500, null=True, blank=True)   

    # ie Museum Holiday Party 
    event_date_title = models.CharField(max_length=500, null=True, blank=True)  

    def display_amount(self):
        amount_str = ""

        if self.donation_type == "e":  
            amount_str = "%s" % ('${:,.2f}'.format(self.amount_exact).rstrip('0').rstrip('.'))        
        elif self.donation_type == "r":
            amount_str = "%s - %s" % ('${:,.2f}'.format(self.amount_range_low).rstrip('0').rstrip('.'), '${:,.2f}'.format(self.amount_range_high).rstrip('0').rstrip('.'))
        elif self.donation_type == "p":
            amount_str = "%s and above" % ('${:,.2f}'.format(self.amount_range_low).rstrip('0').rstrip('.'))
        elif self.donation_type == "o":
            amount_str = self.amount_other        
        elif self.donation_type == "u":
            amount_str = "Unknown"

        return amount_str
          
    def __str__(self):
        if hasattr(self.person, "name"):
            thisName = self.person.name
        else:
            thisName = "No Name" 

        return '%s (%s)' % (thisName,self.institution)


@python_2_unicode_compatible
class Donorgroup(models.Model):
    name = models.CharField(max_length=200, help_text="Name of the group of donors")

    year = models.IntegerField(null=True, blank=True, help_text="Year of this group")

    institution = models.ForeignKey('Institution', on_delete=models.SET_NULL, null=True) 
    
    def get_absolute_url(self):
        return reverse('donorgroup-detail', args=[str(self.id)])

    def __str__(self):
        # String for representing the Model object (in Admin site etc.)
        return self.name


@python_2_unicode_compatible
class Institution(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    image = models.URLField(null=True, default="http://fpoimg.com/100x100")
    desc = models.TextField(null=True, default=None)
    slug = models.SlugField(null=True, default=None, unique=True)  
    
    # TODO make the slug save automatically using AutoSlugField or slugify

    def get_absolute_url(self):
        return reverse('institution-detail', args=[str(self.slug)])

    def __str__(self):
        #String for representing the Model object.
        return self.name
