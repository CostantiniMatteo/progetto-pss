import operator as op

from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.db import transaction

from ..models import Item
from IPython import embed

@transaction.atomic
def item(request, pk):
    item = get_object_or_404(Item, pk=pk)

    try:
        if item.collection.pk not in request.session['labelling']:
            raise PermissionDenied()
    except KeyError:
        raise PermissionDenied()

    if request.method == 'POST':
        if True:
            # Cose
            choice = 'hardcoded'
            item.labels[choice] += 1
            item.votes_number += 1
            item.label = max(item.labels.iteritems(), key=op.itemgetter(1))[0]
            item.save()

            next_item_url = _get_next_item_url(request)
            return redirect(next_item_url)
    else:
        form = { 'image': item.image, 'labels': item.collection.labels }


    return render(request, 'item.html', {'form': form})


def _get_next_item_url(request):
    return 'https://localhost:8000/item/2'
