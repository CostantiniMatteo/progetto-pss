from django.views import generic
from django.contrib.auth.models import User

from ..models import Collection


class CollectionsView(generic.ListView):
    template_name = 'my_collections.html'
    context_object_name = 'collections_list'

    def get_queryset(self):
        return Collection.objects.filter(user=self.request.user)
