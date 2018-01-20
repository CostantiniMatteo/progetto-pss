import random

from django.shortcuts import render, redirect, get_object_or_404
from django.http import  Http404
from django.core.exceptions import PermissionDenied
from django.db import transaction
from django.shortcuts import redirect
from django.urls import reverse

from ..models import Item

@transaction.atomic
def item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    collection = item.collection


    if collection.pk not in request.session.get('labelling', {}):
        raise PermissionDenied()


    if request.method == 'POST':
        try:
            choice = request.POST.dict()['label']
        except KeyError:
            form = {
                        'image': item.name,
                        'labels': item.collection.labels,
                        'error': 'Please, select a label'
                    }
            return render(request, 'item.html', { 'form': form })

        if not item.is_valid_label(choice):
            raise ValueError('Label not valid')

        item.add_vote(choice)
        # Count as a new labelled image only the first time
        if item.votes_number == 1:
            collection.increase_labelled_count(1)
            collection.save()
        item.save()

        next_item_url = get_next_item_url(request, item.collection)
        return redirect(next_item_url)
    else:
        form = { 'image': item.name, 'labels': item.collection.labels }

    return render(request, 'item.html', { 'form': form })


def get_next_item_url(request, collection):
    try:
        if request.session['fetched_items'][collection.pk]:
            next_item = request.session['fetched_items'][collection.pk].pop(0)

            return reverse('item', args=[next_item.pk])
        else:
            _fetch_items(request, collection)
    except KeyError:
        request.session['fetched_items'] = {}
        _fetch_items(request, collection)

    if request.session['fetched_items'][collection.pk]:
        try:
            request.session['labelling'].append(collection.pk)
        except:
            request.session['labelling'] = [collection.pk]

        next_item = request.session['fetched_items'][collection.pk].pop()
        return reverse('item', args=[next_item.pk])
    else:
        raise Http404()


def _fetch_items(request, collection):
    """
    Fetch up to 50 items and save them in session to avoid querying the
    database at every request.
    """
    tmp = list(collection.item_set.order_by('votes_number')[:200])

    fetched_items = []
    left = []
    if tmp:
        # First, take all the items with fewer votes so that every item
        # will be seen at least once before showing the images again.
        min_votes = tmp[0].votes_number

        for item in tmp:
            if item.votes_number == min_votes and len(fetched_items) < 50:
                fetched_items.append(item)
            else:
                left.append(item)

        # Then randomly fetch the others
        if len(fetched_items) < 50 and left:
            random.shuffle(left)
            fetched_items += left[:50 - len(fetched_items)]

    request.session['fetched_items'][collection.pk] = fetched_items
