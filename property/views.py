from rest_framework.generics import ListAPIView, CreateAPIView

from property.models import Property
from property.serializers import PropertySimpleSerializer


class PropertyListView(ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySimpleSerializer


class PropertyCreateView(CreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySimpleSerializer
