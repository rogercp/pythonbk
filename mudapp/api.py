from rest_framework import serializers,viewsets
from .models import Map


class MapSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model=Map
        fields=('title','content')


class MapViewSet(viewsets.ModelViewSet):
    serializer_class = MapSerializer
    queryset = Map.objects.all()