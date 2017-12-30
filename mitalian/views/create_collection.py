from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from ..forms import CollectionForm


@login_required
def create_collection(request):
    if request.method == 'POST':
        form = CollectionForm(request.POST)
        if form.is_valid():
            collection = form.save(commit=False)

            if len(collection.labels) > len(set(collection.labels)):
                form.add_error('labels', 'All labels must be unique')
                return render(request,
                              'create_collection.html',
                              { 'form': form })

            collection.init(request.user)
            collection.save()
            # ^ We need to call save() first to get a primary-key
            relative_url = '/begin-labelling/%d' % collection.pk
            collection.link = request.build_absolute_uri(relative_url)
            collection.save()

            return redirect('../update-collection/{}'.format(collection.pk))
    else:
        form = CollectionForm()

    return render(request, 'create_collection.html', { 'form': form })
