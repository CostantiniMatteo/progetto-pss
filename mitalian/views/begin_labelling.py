from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User

from ..forms import BeginLabellingForm
from ..models import Collection


def begin_labelling(request, pk):
    if request.method == 'POST':
        form = BeginLabellingForm(request.POST)
        if form.is_valid():
            # Check password
            collection = get_object_or_404(Collection, pk=pk)
            if collection.password != form.cleaned_data.get('password'):
                raise HttpResponseForbidden()

            # Load images
            fetched_items = collection.item_set.order_by('-last_fetched')[:50]
            request.session['fetched_items'] = fetched_items

            # Redirect to the first one
            if len(fetched_items) > 0:
                # TODO: Add a cookie
                return redirect('../item/{}'.format(fetched_items[0].pk))
            else:
                # TODO: Maybe a page saying that the collection is empty
                return redirect('../home')
    else:
        form = BeginLabellingForm()
    return render(request, 'begin_labelling.html', {'form': form})
