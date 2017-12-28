from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect

from ..models import Collection, Item


def truncate_collection(request, pk):
    collection = get_object_or_404(Collection, pk=pk)
    if request.user != collection.user:
        raise PermissionDenied()

    Item.objects.filter(collection=collection).delete()

    collection.total_images = 0
    collection.labelled_images = 0
    collection.progress = 0
    collection.save()

    return redirect('.')
