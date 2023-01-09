from q_school.geography.models import Region
from rest_framework import serializers

class RegionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Region
        fields = ['name', 'associated_city', 'associated_country', 'associated_territory', 'description', 'nanatan', 'weasel_shaker']