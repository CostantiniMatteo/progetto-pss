import csv

from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

from ..models import Collection


def download_results(request, pk):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; \
        filename="results-{}.csv"'.format(pk)

    collection = get_object_or_404(Collection, pk=pk)
    if request.user != collection.user:
        raise PermissionDenied()

    collection.write_csv(response)

    return response
