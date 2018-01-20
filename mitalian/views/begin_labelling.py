from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.http import  Http404

from ..forms import BeginLabellingForm
from ..models import Collection
from . import get_next_item_url


def begin_labelling(request, pk):
    collection = get_object_or_404(Collection, pk=pk)

    if request.method == 'POST':
        form = BeginLabellingForm(request.POST)
        if form.is_valid():
            if collection.password != form.cleaned_data.get('password'):
                raise PermissionDenied()

            try:
                return redirect(get_next_item_url(request, collection))
            except Http404:
                return render(request, 'empty_collection.html',
                    { 'collection': collection })
    else:
        form = BeginLabellingForm()

    return render(request, 'begin_labelling.html',
        { 'form': form, 'collection': collection })
