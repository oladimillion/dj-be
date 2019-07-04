from django.db import models
from django.utils.translation import ugettext_lazy as _


class ShippingRegion(models.Model):
    shipping_region = models.CharField(_('shipping_region'), max_length=100, blank=True)

    class Meta:
        db_table = 'shipping_region'

    def __str__(self):
        return self.shipping_region or 'n/a'
