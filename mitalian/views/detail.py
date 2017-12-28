from django.views import generic
from django.contrib.auth.models import User
from django.http import  Http404
from django.core.exceptions import PermissionDenied

from ..models import Collection, Item


class CollectionDetailView(generic.DetailView):
    model = Collection
    template_name = 'detail.html'
    context_object_name = 'collection'


    def get_queryset(self):
        queryset = Collection.objects.filter(pk=self.kwargs['pk'])

        if len(queryset) > 0:
            collection = queryset.first()
        else:
            raise Http404()

        if collection.user != self.request.user:
            raise PermissionDenied()

        return queryset;
