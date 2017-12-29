import os
from zipfile import ZipFile
from io import BytesIO

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseServerError
from django.core.exceptions import PermissionDenied
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

from ..models import Collection, Item
from ..forms import UpdateCollectionForm


def update_collection(request, pk):
    if not request.user.is_authenticated:
        return redirect('../login')

    collection = get_object_or_404(Collection, pk=pk)

    if request.method == 'POST':
        form = UpdateCollectionForm(request.POST, request.FILES)
        if form.is_valid():
            zip_file = ZipFile(request.FILES['zip_file'])
            # for name in zip_file.namelist():
            #     data = zip_file.read(name)

            #     try:
            #         from PIL import Image
            #         image = Image.open(BytesIO(data))
            #         image.load()
            #     except:
            #         # TODO: Redirect to an error message
            #         raise Exception()

            #     name = os.path.split(name)[1]
            #     path = os.path.join(settings.MEDIA_ROOT,
            #                         name)
            #     saved_path = default_storage.save(path, ContentFile(data))

            #     item = Item(name=name,
            #                 collection=collection,
            #                 label='',
            #                 labels={k: 0 for k in collection.labels},
            #                 votes_number=0,
            #                 image=saved_path)
            #     item.save()

            # Update images count
            # collection.total_images += len(zip_file.infolist())
            collection.update(zip_file)
            collection.save()
            return redirect('../detail/%d' % collection.pk)

        elif collection.user != request.user:
            raise PermissionDenied()

    else:
        form = UpdateCollectionForm()

    return render(request,
                  'update_collection.html',
                  {
                    'form': form,
                    'collection': collection,
                  })
