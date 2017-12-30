import os
import csv
from io import BytesIO

from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings


class Collection(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_images = models.IntegerField()
    labelled_images = models.IntegerField()
    # Allowed labels for collection's images
    labels = ArrayField(models.CharField(max_length=256))
    # Where you can label images of this collection
    link = models.URLField()
    # Password required to labels images of this collection
    password = models.TextField()

    @property
    def progress(self):
        if self.total_images == 0:
            return 0

        return int(self.labelled_images / self.total_images * 100)

    def init(self, user):
        self.user = user
        self.total_images = 0
        self.labelled_images = 0
        password = User.objects.make_random_password(length=10)
        self.password = password

    # Would be nice to use F() expressions which are faster
    def increase_labelled_count(self, count):
        self.labelled_images += count;


    def truncate(self):
        # Import here to avoid recursive import
        from . import Item

        Item.objects.filter(collection=self).delete()

        self.total_images = 0
        self.labelled_images = 0


    def update(self, zip_file):
        # Import here to avoid recursive import
        from . import Item

        for name in zip_file.namelist():
            data = zip_file.read(name)

            try:
                from PIL import Image
                image = Image.open(BytesIO(data))
                image.load()
            except:
                raise ValueError('Zip must contain only images')

            name = os.path.split(name)[1]
            path = os.path.join(settings.MEDIA_ROOT,
                                name)
            saved_path = default_storage.save(path, ContentFile(data))

            item = Item(name=name,
                        collection=self,
                        label='',
                        labels={k: 0 for k in self.labels},
                        votes_number=0,
                        image=saved_path)
            item.save()
            self.total_images += 1


    def write_csv(self, out):
        # / can't be used in filenames so we are sure that a / can only appear
        # as a separator
        writer = csv.writer(out, delimiter='/')
        images = self.item_set.all()
        for image in images:
            if image.label is None:
                writer.writerow([image.name, ''])
            else:
                writer.writerow([image.name, image.label])


    def __str__(self):
        return self.name
