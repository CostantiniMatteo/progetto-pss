from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from ..models import Collection


@login_required
def delete_collection(request, pk):
    collection = get_object_or_404(Collection, pk=pk)

    if request.user != collection.user:
        raise PermissionDenied()

    collection.delete()

    return redirect('collections')
