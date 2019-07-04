from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from .shipping_region import ShippingRegion


from ..managers import UserManager

class Customer(PermissionsMixin, AbstractBaseUser):
    customer = models.AutoField(primary_key=True)
    name = models.CharField(_('name'), max_length=50, unique=True)
    email = models.EmailField(_('email address'),  max_length=100, unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_staff = models.BooleanField(_('staff'), default=False)
    is_superuser = models.BooleanField(_('superuser'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    credit_card = models.CharField(_('credit_card'), max_length=100, blank=True)
    address_1 = models.CharField(_('address one'), max_length=100, blank=True)
    address_2 = models.CharField(_('address two'), max_length=100, blank=True)
    city = models.CharField(_('city'), max_length=100, blank=True)
    region = models.CharField(_('region'), max_length=100, blank=True)
    postal_code = models.CharField(_('postal code'), max_length=100, blank=True)
    country = models.CharField(_('country'), max_length=100, blank=True)
    day_phone = models.CharField(_('day phone'), max_length=100, blank=True)
    eve_phone = models.CharField(_('evening phone'), max_length=100, blank=True)
    mob_phone = models.CharField(_('mobile phone'), max_length=100, blank=True)
    shipping_region = models.ForeignKey(ShippingRegion, default=1, on_delete=models.CASCADE, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('customer')
        verbose_name_plural = _('customers')

    def __str__(self):
        return self.email
