from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect

from ..models import Collection


def delete_collection(request, pk):
    collection = get_object_or_404(Collection, pk=pk)

    if request.user != collection.user:
        raise PermissionDenied()

    collection.delete()

    return redirect('../collections')
