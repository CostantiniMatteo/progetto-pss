from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from ..models import Collection


@login_required
def truncate_collection(request, pk):
    collection = get_object_or_404(Collection, pk=pk)
    if request.user != collection.user:
        raise PermissionDenied()

    collection.truncate()
    collection.save()

    return redirect('collections')
