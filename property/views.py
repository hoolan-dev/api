from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListAPIView, CreateAPIView

from property.models import Property
from property.serializers import PropertySimpleSerializer


class PropertyListView(ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySimpleSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['catastro_id', 'id', 'solana_id', 'ref_collection', 'form_id', ]
    search_fields = [
        'contributor__name',
        'contributor__identification',
        'contributor__type',
        'contributor__property',
        'contributor__quality',
        'contributor__address',
        'contributor__city',
        'identification',
    ]


class PropertyCreateView(CreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySimpleSerializer
