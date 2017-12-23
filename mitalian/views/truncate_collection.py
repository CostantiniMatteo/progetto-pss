from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect

from ..models import Collection, Item

def truncate_collection(request, pk):
    response = HttpResponse(content_type='')
    collection = get_object_or_404(Collection, pk=pk)

    if request.user != collection.user:
        raise HttpResponseForbidden()

    Item.objects.filter(collection=collection).delete()

    return redirect('./my-collections')