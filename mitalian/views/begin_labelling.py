from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied

from ..forms import BeginLabellingForm
from ..models import Collection
from . import get_next_item_url


# TOOD: Check if this works even if the user is not logged in
def begin_labelling(request, pk):
    if request.method == 'POST':
        form = BeginLabellingForm(request.POST)
        if form.is_valid():
            # Check password
            collection = get_object_or_404(Collection, pk=pk)
            if collection.password != form.cleaned_data.get('password'):
                raise PermissionDenied()

            return redirect(get_next_item_url(request, collection))
    else:
        form = BeginLabellingForm()

    return render(request, 'begin_labelling.html', {'form': form})
