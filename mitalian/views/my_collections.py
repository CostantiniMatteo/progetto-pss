from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from ..models import Collection


class CollectionsView(LoginRequiredMixin, generic.ListView):
    template_name = 'my_collections.html'
    context_object_name = 'collections_list'

    def get_queryset(self):
        return Collection.objects.filter(user=self.request.user)
