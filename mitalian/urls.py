"""mitalian URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.http import HttpResponseRedirect

from .views import index, signup, CollectionsView, CollectionDetailView
from .views import create_collection, update_collection, item, download_results
from .views import truncate_collection, begin_labelling, delete_collection


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda r: HttpResponseRedirect('home/'), name='root'),
    path('home/', index, name='index'),
    path('login/', auth_views.login, {'template_name': 'login.html', 'redirect_authenticated_user': True}, name='login'),
    path('logout/', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    path('signup/', signup, name='signup'),
    path('collections/', CollectionsView.as_view(), name='collections'),
    path('create-collection/', create_collection, name='create-collection'),
    path('update-collection/<int:pk>', update_collection, name='update-collection'),
    path('download-results/<int:pk>', download_results, name='download-results'),
    path('detail/<int:pk>', CollectionDetailView.as_view(), name='detail'),
    path('begin-labelling/<int:pk>', begin_labelling, name='begin-labelling'),
    path('item/<int:pk>', item, name='item'),
    path('truncate-collection/<int:pk>', truncate_collection, name='truncate-collection'),
    path('delete-collection/<int:pk>', delete_collection, name='delete-collection'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
