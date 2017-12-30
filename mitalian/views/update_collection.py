import os
from zipfile import ZipFile
from io import BytesIO

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseServerError
from django.core.exceptions import PermissionDenied
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from django.contrib.auth.decorators import login_required

from ..models import Collection, Item
from ..forms import UpdateCollectionForm


@login_required
def update_collection(request, pk):
    collection = get_object_or_404(Collection, pk=pk)

    if collection.user != request.user:
        raise PermissionDenied()

    if request.method == 'POST':
        form = UpdateCollectionForm(request.POST, request.FILES)
        if form.is_valid():
            zip_file = ZipFile(request.FILES['zip_file'])

            collection.update(zip_file)
            collection.save()

            return redirect('../detail/%d' % collection.pk)
    else:
        form = UpdateCollectionForm()

    return render(request,
                  'update_collection.html',
                  {
                    'form': form,
                    'collection': collection,
                  })
