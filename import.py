# python manage.py shell < import.py

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "catalog.settings")

print("Running import script")

# Donation.objects.all().delete()
# Donation.objects.filter(donation_date="2011-07-01").delete()

def get_all_products(whichfile):
    from catalog.models import Person, Donation, Donorgroup, Institution
    import csv
    from itertools import islice
    fp = open(whichfile,'r')
    # You can also put relative path of csv file with respect to    
    # manage.py file
    csvOut = csv.reader(fp, delimiter=',')
    savedCount = 0

    # islice skips the first row of the csv
    for line in islice(csvOut, 1, None):

        # replace empty strings with None
        for n,i in enumerate(line):
            if i=="":
                line[n]=None 

        # search for user
        this_person = line[0]
        p1DoesExist = ""
        p1DoesExist = Person.objects.filter(name=this_person)
        if len(p1DoesExist) == 0:
            p1 = Person(name=this_person)
            p1.save()
            print("new person %s" % line[0])
        else:
            p1 = p1DoesExist[0]
            print("duplicate person %s" % line[0])

        # search for institution
        this_institution = line[3]
        i1DoesExist = Institution.objects.filter(name=this_institution)
        if len(i1DoesExist) == 0:
            i1 = Institution(name=this_institution)
            i1.save()
            print("new institution %s" % line[3])
        else:
            i1 = i1DoesExist[0]
            print("duplicate institution %s" % line[3])

        # search for Donorgroup
        this_donorgroup = line[4]
        Dg1DoesExist = Donorgroup.objects.filter(name=this_donorgroup)
        if len(Dg1DoesExist) == 0:
            dg1 = Donorgroup(name=this_donorgroup)
            dg1.save()
            print("new donorgroup %s" % line[4])
        else:
            dg1 = Dg1DoesExist[0]
            print("duplicate donorgroup %s" % line[4])

        d1 = Donation(
            donation_full_name=line[1],
            event_name=line[2],
            donation_type=line[5],
            amount_exact=line[6],
            amount_range_low=line[7],
            amount_range_high=line[8],
            amount_other=line[9],
            donation_date_start=line[10],
            donation_date_end=line[11],
            collection_date=line[12],
            data_source_name=line[13],
            data_source_url=line[14],
            donation_class=line[15],
            person=p1,
            institution=i1,
            donorgroup=dg1
        )
        try:
            d1.save()
            print("Saved:", savedCount)
            savedCount += 1
        except:
            print("Unexpected error")
            break

    print("saved %s donations" % savedCount)


get_all_products('imported_data/Museum Data Template - D3- MAH in Santa Cruz 2011-2012 Annual Report (2).csv')

