from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password

from ..models import Collection
from ..forms import CollectionForm

# TODO: Cambiare il modo in cui vengono inserite le label
# TODO: Controllare che label non siano duplicate
def create_collection(request):
    if request.method == 'POST':
        form = CollectionForm(request.POST)
        if form.is_valid():
            collection = form.save(commit=False)
            collection.user = request.user
            collection.progress = 0
            password = User.objects.make_random_password(length=10)
            collection.password_hash = password

            collection.save()
            collection.link = '/labelling/%d' % collection.pk
            collection.save()

            # TODO: Redirect a update-collection
            return redirect('../detail/{}'.format(collection.pk))
    else:
        form = CollectionForm()

    return render(request, 'create_collection.html', {'form': form})
