# python manage.py shell < import.py
# execfile('import.py')

# change path depending on what you want to import
mypath = 'imported_data/003'


import os, sys
import glob

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "catalog.settings")


'''
from catalog.models import Person, Donation, Donorgroup, Institution
Person.objects.all().delete()
Donation.objects.all().delete()
Donorgroup.objects.all().delete()
Institution.objects.all().delete()
Donation.objects.filter(donation_date="2011-07-01").delete()
'''

def importCsv(whichfile):
    print("Importing: ", whichfile)

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
        i1 = None
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
            dg1 = Donorgroup(name=this_donorgroup, institution=i1)
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
            donation_list=line[16],
            event_date_title=line[17],
            person=p1,
            institution=i1,
            donorgroup=dg1
        )
        # d1.save()
        # break

        try:
            d1.save()
            print("Saved:", savedCount)
            savedCount += 1
        except:
            print("Unexpected error")
            break

    print("saved %s donations" % savedCount)


# importCsv('imported_data/Museum Data Template - 1985-1989 NYC Public Library.csv')


def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")


def confirmRun():
    # lists all the files in a directory
    onlyfiles = glob.glob(mypath+'/*.csv')
    question = "Import %s CSV files from %s" % (len(onlyfiles), mypath)
    result = query_yes_no(question)

    if result is True:
        for f in onlyfiles:
            print('importinggggg - ', f)
            importCsv(f)


confirmRun()    
