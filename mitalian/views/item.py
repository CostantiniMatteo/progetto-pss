import operator as op
import random

from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.db import transaction

from ..models import Item
from IPython import embed

@transaction.atomic
def item(request, pk):
    embed()
    item = get_object_or_404 (Item, pk=pk)

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

            next_item_url = get_next_item_url(request, item.collection)
            return redirect(next_item_url)
    else:
        form = { 'image': item.name, 'labels': item.collection.labels }

    return render(request, 'item.html', {'form': form})


def get_next_item_url(request, collection):
    # Load images
    try:
        if request.session['fetched_items']:
            next_item = request.session['fetched_items'].pop()

            return '../item/{}'.format(next_item.pk)
        else:
            _fetch_items(request, collection)
    except KeyError:
        _fetch_items(request, collection)

    if request.session['fetched_items']:
        try:
            request.session['labelling'].append(collection.pk)
        except:
            request.session['labelling'] = [collection.pk]

        next_item = request.session['fetched_items'].pop()
        return '../item/{}'.format(next_item.pk)
    else:
        # TODO: Maybe a page saying that the collection is empty
        # See Django Forms error messages
        return '../home'


def _fetch_items(request, collection):
    fetched_items = list(collection.item_set.order_by('-votes_number')[:200])
    random.shuffle(fetched_items)
    fetched_items = fetched_items[:50]
    request.session['fetched_items'] = fetched_items
