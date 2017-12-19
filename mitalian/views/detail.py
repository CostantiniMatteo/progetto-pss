from django.views import generic
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from ..models import Collection, Item

# class CollectionDetailView(generic.ListView):
#     template_name = 'detail.html'
#     context_object_name = 'collection'


#     def get_queryset(self):
#         collection = Collection.objects.get()
#         if collection.user != self.request.user:
#             raise HttpResponseForbidden()

#         return collection;

class CollectionDetailView(generic.DetailView):
    model = Collection
    template_name = 'detail.html'
