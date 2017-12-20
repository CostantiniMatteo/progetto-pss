from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from ..models import Collection, Item

def download_results(request, pk):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    collection = Collection.objects.get(pk=pk)

    if request.user != collection.user:
        raise HttpResponseForbidden()

    # Iterate over item_set and write out
    writer = csv.writer(response, delimiter=' ')
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response
