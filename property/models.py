import uuid

from django.db import models


class Contributor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.JSONField(null=True, blank=True)
    identification = models.JSONField(null=True, blank=True)
    name = models.JSONField(null=True, blank=True)
    property = models.JSONField(null=True, blank=True)
    quality = models.JSONField(null=True, blank=True)
    address = models.JSONField(null=True, blank=True)
    city = models.JSONField(null=True, blank=True)

    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    

class Property(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    catastro_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    solana_id = models.CharField(max_length=100, null=True, blank=True, unique=True)
    ref_collection = models.CharField(max_length=100, null=True, blank=True)
    identification = models.JSONField(null=True, blank=True)
    form_id = models.CharField(max_length=100, null=True, blank=True)
    contributor = models.ForeignKey(Contributor, null=True, blank=True, on_delete=models.CASCADE, related_name='contributor')

    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        super(Property, self).save(*args, **kwargs)
