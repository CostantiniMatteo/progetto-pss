import csv

from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

from ..models import Collection


def download_results(request, pk):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'


    collection = get_object_or_404(Collection, pk=pk)
    if request.user != collection.user:
        raise PermissionDenied()

    images = collection.item_set.all()

    # / can't be used in filenames so we are sure that a / can only appear
    # as a separator
    writer = csv.writer(response, delimiter='/')
    for image in images:
        if image.label is None:
            writer.writerow([image.name, ''])
        else:
            writer.writerow([image.name, image.label])

    return response
