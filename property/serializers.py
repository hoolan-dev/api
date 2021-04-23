from rest_framework import serializers

from property.models import Property


class PropertySimpleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Property
        fields = ('id', 'catastro_id', 'solana_id',)
