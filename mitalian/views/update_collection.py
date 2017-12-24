import datetime, os
from zipfile import ZipFile
from io import BytesIO
from IPython import embed

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden, HttpResponseServerError
from django.contrib.auth.models import User
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

            for name in zip_file.namelist():
                data = zip_file.read(name)
                try:
                    from PIL import Image
                    image = Image.open(BytesIO(data))
                    image.load()
                    image = Image.open(BytesIO(data))
                    image.verify()
                except:
                    raise HttpResponseServerError()
                name = os.path.split(name)[1]
                path = os.path.join(settings.MEDIA_ROOT,
                                    name)
                saved_path = default_storage.save(path, ContentFile(data))

                # TODO: Init labels field, possibly defining a function
                item = Item(name=name,
                            collection=collection,
                            label='',
                            labels={k: 0 for k in collection.labels},
                            last_fetched=None,
                            image=saved_path)
                item.save()


            # embed()
            # Using File
            # f = open('/path/to/file')
            # self.license_file.save(new_name, File(f))
            # Using ContentFile
            # self.license_file.save(new_name, ContentFile('A string with the file content'))

            # Unzip file
            # Check all images
            # Save every image
            return redirect('../detail/%d' % collection.pk)
    else:
        if collection.user != request.user:
            raise HttpResponseForbidden()

        form = UpdateCollectionForm()

    return render(request,
                  'update_collection.html',
                  {
                    'form': form,
                    'collection': collection,
                  })
