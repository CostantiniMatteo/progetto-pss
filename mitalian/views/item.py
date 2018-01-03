import random

from django.shortcuts import render, redirect, get_object_or_404
from django.http import  Http404
from django.core.exceptions import PermissionDenied
from django.db import transaction

from ..models import Item


@transaction.atomic
def item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    collection = item.collection

    try:
        if collection.pk not in request.session['labelling']:
            raise PermissionDenied()
    except KeyError:
        raise PermissionDenied()

    if request.method == 'POST':
        try:
            choice = request.POST.dict()['label']
        except KeyError:
            form = {
                        'image': item.name,
                        'labels': item.collection.labels,
                        'error': 'Please, select a label' }
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
            next_item = request.session['fetched_items'][collection.pk].pop()

            return '../item/{}'.format(next_item.pk)
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
        return '../item/{}'.format(next_item.pk)
    else:
        raise Http404()


def _fetch_items(request, collection):
    """
    Fetch up to 50 items and save them in session to avoid querying the
    database at every request.
    """
    tmp = list(collection.item_set.order_by('-votes_number')[:200])

    fetched_items = []
    # First, take all the items with fewer votes so that very item will
    # be seen at least once before showing the images again.
    min_votes = min(tmp, key=lambda x: x.votes_number).votes_number
    fetched_items = [item for item in tmp if item.votes_number == min_votes
                        and not tmp.remove(item)]
    # for item in tmp:
    #     if item.votes_number == min_votes:
    #         tmp.remove(item)
    #         fetched_items.append(item)

    # Then randomly fetch the others
    if len(fetched_items) < 50 and tmp:
        random.shuffle(tmp)
        fetched_items += tmp[:50 - len(fetched_items)]

    request.session['fetched_items'][collection.pk] = fetched_items
