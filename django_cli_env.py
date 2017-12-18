import os, sys
import django

sys.path.append('/mitalian')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mitalian.settings'

django.setup()

from django.contrib.auth.models import User
from mitalian.models import Collection, Item

