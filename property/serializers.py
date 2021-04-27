from rest_framework import serializers

from property.models import Property, Contributor


class ContributorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contributor
        fields = ('id', 'type', 'identification', 'name', 'property', 'quality', 'address', 'city')


class PropertySimpleSerializer(serializers.HyperlinkedModelSerializer):
    contributor = ContributorSerializer()

    class Meta:
        model = Property
        fields = ('id', 'contributor', 'form_id', 'catastro_id', 'solana_id', 'ref_collection', 'identification')

    def create(self, validated_data):
        contributor, c_created = Contributor.objects.get_or_create(**validated_data['contributor'])
        validated_data.pop('contributor')
        instance = Property.objects.create(contributor=contributor, **validated_data)
        return instance
