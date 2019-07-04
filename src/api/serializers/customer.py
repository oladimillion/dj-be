from rest_framework import serializers
from .. import models

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Customer
        fields = ('url', 'username', 'email', 'is_staff')
