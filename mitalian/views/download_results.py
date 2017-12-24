import csv

from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from ..models import Collection, Item

def download_results(request, pk):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    collection = get_object_or_404(Collection, pk=pk)

    if request.user != collection.user:
        raise HttpResponseForbidden()

    writer = csv.writer(response, delimiter=' ')
    images = collection.item_set.all()
    # Implement here
    # Iterate over item_set and write out
    for image in images:
        if image.label is None:
            writer.writerow([image.name, ''])
        else:
            writer.writerow([image.name, image.label])

    # writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    # writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response
