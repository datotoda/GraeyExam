from django.db import models
from django.utils.translation import ugettext_lazy as _


class Ticket(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Ticket name'))
    price = models.DecimalField(max_digits=4, decimal_places=2)
    start_date = models.DateTimeField(verbose_name=_('Start time'))
    end_date = models.DateTimeField(verbose_name=_('End time'), null=True, blank=True)
    barcode = models.CharField(max_length=16, verbose_name=_('Barcode'), unique=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    ticker = models.OneToOneField(to='Ticket', related_name='orders', on_delete=models.PROTECT,)
    user = models.ForeignKey(to='user.User', on_delete=models.SET_NULL, null=True, related_name='orders')

    def __str__(self):
        return f'{self.user} - {self.ticket}'

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')
