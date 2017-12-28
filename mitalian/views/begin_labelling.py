import random

from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied

from ..forms import BeginLabellingForm
from ..models import Collection


# TOOD: Check if this works even if the user is not logged in
def begin_labelling(request, pk):
    if request.method == 'POST':
        form = BeginLabellingForm(request.POST)
        if form.is_valid():
            # Check password
            collection = get_object_or_404(Collection, pk=pk)
            if collection.password != form.cleaned_data.get('password'):
                raise PermissionDenied()

            # Load images
            fetched_items = collection.item_set.order_by('-votes_number')[:200]
            random.shuffle(fetched_items)
            fetched_items = fetched_items[:50]
            request.session['fetched_items'] = list(fetched_items)

            # Redirect to the first one
            if len(fetched_items) > 0:
                try:
                    request.session['labelling'].append(collection.name)
                except:
                    request.session['labelling'] = [collection.name]

                return redirect('../item/{}'.format(fetched_items[0].pk))
            else:
                # TODO: Maybe a page saying that the collection is empty
                # See Django Forms error messages
                return redirect('../home')
    else:
        form = BeginLabellingForm()

    return render(request, 'begin_labelling.html', {'form': form})
