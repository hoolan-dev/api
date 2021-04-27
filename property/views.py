from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, CreateAPIView

from property.models import Property
from property.serializers import PropertySimpleSerializer


class PropertyListView(ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySimpleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['catastro_id', 'id', 'solana_id', 'ref_collection', 'form_id', ]


class PropertyCreateView(CreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySimpleSerializer
