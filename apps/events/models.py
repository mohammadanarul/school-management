from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.helpers.models import BaseEntity


class Event(BaseEntity):
    session_year = models.SmallIntegerField(_("session year"), help_text="")
    name = models.CharField(_("name"), max_length=255)
    banner = models.ImageField(_("banner"), upload_to="event/banners/")
    group_image = models.ImageField(_("group image"), upload_to="event/group-images/")
    date = models.DateField(_("date"))
    cost_balance = models.FloatField(_("cost balance"), null=True, blank=True)

    def __str__(self):
        return self.name
