from django.views import generic
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404

from ..models import Collection, Item
from IPython import embed


# class CollectionDetailView(generic.ListView):
#     template_name = 'detail.html'
#     context_object_name = 'collection'


#     def get_queryset(self):
#         embed()
#         collection = get_object_or_404(Collection, pk=self.request['pk'])
#         if collection.user != self.request.user:
#             raise HttpResponseForbidden()

#         return collection;

class CollectionDetailView(generic.DetailView):
    model = Collection
    template_name = 'detail.html'
