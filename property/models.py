import uuid

from django.db import models


class Property(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    catastro_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    solana_id = models.CharField(max_length=100, null=True, blank=True, unique=True)

    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        print('')

        super(Property, self).save(*args, **kwargs)
