from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest

from ..forms import CollectionForm

def create_collection(request):
    if request.method == 'POST':
        form = CollectionForm(request.POST)
        if form.is_valid():
            collection = form.save(commit=False)

            if len(collection.labels) > len(set(collection.labels)):
                # TODO: Terrible. Find another way.
                raise HttpResponseBadRequest("Labels contain duplicates")

            collection.user = request.user
            collection.progress = 50
            collection.total_images = 0
            collection.labelled_images = 0
            password = User.objects.make_random_password(length=10)
            collection.password = password

            collection.save()
            relative_url = '/labelling/%d' % collection.pk
            collection.link = request.build_absolute_uri(relative_url)
            collection.save()

            return redirect('../update-collection/{}'.format(collection.pk))
    else:
        form = CollectionForm()

    return render(request, 'create_collection.html', {'form': form})
