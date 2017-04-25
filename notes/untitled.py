api post to /import
all async


setup admin only upload page
setup django async rest stuff
get upload button working


----
backup db
if success
run import script 
if error, restore db


looks promosing
https://django-dbbackup.readthedocs.io/en/stable/commands.html
https://github.com/django-backup/django-backup

heroku only:
https://devcenter.heroku.com/articles/heroku-postgres-import-export




from catalog.models import Snippet
from catalog.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

snippet = Snippet(code='foo = "bar"\n')
snippet.save()

snippet = Snippet(code='print "hello, world"\n')
snippet.save()

serializer = SnippetSerializer(snippet)
serializer.data
# {'id': 2, 'title': u'', 'code': u'print "hello, world"\n', 'linenos': False, 'language': u'python', 'style': u'friendly'}

content = JSONRenderer().render(serializer.data)
content
# '{"id": 2, "title": "", "code": "print \\"hello, world\\"\\n", "linenos": false, "language": "python", "style": "friendly"}'

from django.utils.six import BytesIO

stream = BytesIO(content)
data = JSONParser().parse(stream)


serializer = SnippetSerializer(data=data)
serializer.is_valid()
# True
serializer.validated_data
# OrderedDict([('title', ''), ('code', 'print "hello, world"\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])
serializer.save()
# <Snippet: Snippet object>



from catalog.serializers import SnippetSerializer
serializer = SnippetSerializer()
print(repr(serializer))

http http://127.0.0.1:8000/catalog/snippets/





for p in Person.objects.raw('SELECT * FROM catalog_person LIMIT 5 '):
    print p.donation

for p in Person.objects.raw('SELECT * FROM catalog_person INNER JOIN Donations ON catalog_person.id=Donations.id'):
    print p



Person.objects.all().order_by('-donation__donation_date_start')
