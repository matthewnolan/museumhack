from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse 
import uuid 


class Person(models.Model):
    name = models.CharField(max_length=300, default="John Doe")

    def get_absolute_url(self):
        return reverse('person-detail', args=[str(self.id)])
    
    def __str__(self):
        return '%s' % (self.name)


class Donation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular donation")

    # Replace Admin Site Foreign Key Field/Dropdown with Textbox?
    # https://groups.google.com/forum/#!topic/django-users/zjdbX5ipRqY
    person = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True) 

    # bill and melinda gates
    donation_full_name = models.CharField(max_length=500, null=True, blank=True)

    # Apollo Circle Benefit 2013
    event_name = models.CharField(max_length=500, null=True, blank=True)

    # ie MOMA
    institution = models.ForeignKey('Institution', on_delete=models.SET_NULL, null=True) 

    # ie Apollo Circle
    donorgroup = models.ForeignKey('Donorgroup', on_delete=models.SET_NULL, null=True) 

    DONATION_TYPES = (
        ('e', 'Exact Value: $100'),
        ('r', 'Range: $100-$200'),
        ('p', 'Range: $100 and above'),
        ('o', 'Just other'),
    )

    donation_type = models.CharField(max_length=1, choices=DONATION_TYPES, default='e', help_text='Donation Type')

    amount_exact = models.DecimalField(max_digits=99, decimal_places=2, default=0, help_text="For exact values ie: $100")
    amount_range_low = models.DecimalField(max_digits=99, decimal_places=2, default=0, help_text="For range low end ie: $100-$200 or for low end of range ie: $100 and above")
    amount_range_high = models.DecimalField(max_digits=99, decimal_places=2, default=0, help_text="For high end $100-$200")

    # Range of amount of money ie  "$500+" or "$1000 to $2000"
    amount_other = models.CharField(max_length=500, null=True, blank=True, help_text="ie: Plus a special gift from our family")


    # Date person donates
    donation_date = models.DateField(null=True, blank=True)

    # Date at which I collected data
    collection_date = models.DateField(null=True, blank=True)

    data_source_name = models.CharField(max_length=500, null=True, blank=True) 

    data_source_url = models.CharField(max_length=500, null=True, blank=True)  

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

        return amount_str
          
    def __str__(self):

        if hasattr(self.person, "name"):
            thisName = self.person.name
        else:
            thisName = "No Name" 

        return '%s (%s)' % (thisName,self.institution)


class Donorgroup(models.Model):
    name = models.CharField(max_length=200, help_text="Name of the group of donors")

    def get_absolute_url(self):

        # Returns the url to access a particular author instance.

        return reverse('donorgroup-detail', args=[str(self.id)])

    def __str__(self):

        # String for representing the Model object (in Admin site etc.)

        return self.name


class Institution(models.Model):

    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100, default="NYC")
    
    def get_absolute_url(self):
        # Returns the url to access a particular author instance.
        return reverse('institution-detail', args=[str(self.id)])
    
    def __str__(self):
        #String for representing the Model object.
        return '%s, %s' % (self.name, self.city)

