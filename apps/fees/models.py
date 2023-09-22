from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.helpers.models import BaseEntity
from apps.helpers.utils import FeeTypes, FeeStatus
from apps.users.models import User


class Fee(BaseEntity):
    user = models.ForeignKey(
        User, verbose_name=_("user"), on_delete=models.CASCADE, related_name="fees"
    )
    object_id = models.BigIntegerField(null=True, blank=True)
    transaction_id = models.CharField(_("transaction id"), max_length=100)
    balance = models.DecimalField(_("balance"), decimal_places=2, max_digits=6)
    type = models.SmallIntegerField(_("type"), choices=FeeTypes.choices)
    status = models.SmallIntegerField(_("status"), choices=FeeStatus.choices)

    def __str__(self):
        return self.get_type_display()
