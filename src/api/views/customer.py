from rest_framework import viewsets

from .. import serializers, models


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer
