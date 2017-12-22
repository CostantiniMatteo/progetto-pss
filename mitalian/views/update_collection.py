from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User

from ..models import Collection, Item
from ..forms import UpdateCollectionForm

def update_collection(request, pk):
    if not request.user.is_authenticated:
        return redirect('../login')

    collection = get_object_or_404(Collection, pk=pk)

    if request.method == 'POST':
        form = UpdateCollectionForm(request.POST)
        if form.is_valid():
            return redirect('../penis')
    else:
        if collection.user != request.user:
            raise HttpResponseForbidden()

        form = UpdateCollectionForm()

    return render(request,
                  'update_collection.html',
                  {
                    'form': form,
                    'collection': collection,
                  })
