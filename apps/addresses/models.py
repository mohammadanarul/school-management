from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.helpers.models import BaseEntity
from apps.users.models import User


class Country(BaseEntity):
    name = models.CharField(_("name"), max_length=150)

    def __str__(self):
        return self.name


class Division(BaseEntity):
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name="divisions"
    )
    name = models.CharField(_("name"), max_length=200)

    def __str__(self):
        return self.name


class District(BaseEntity):
    division = models.ForeignKey(
        Division, on_delete=models.CASCADE, related_name="districts"
    )
    name = models.CharField(_("name"), max_length=200)

    def __str__(self):
        return self.name


class SubDistrict(BaseEntity):
    district = models.ForeignKey(
        District, on_delete=models.CASCADE, related_name="sub_districts"
    )
    name = models.CharField(_("name"), max_length=200)

    def __str__(self):
        return self.name


class Union(BaseEntity):
    sub_district = models.ForeignKey(
        SubDistrict, on_delete=models.CASCADE, related_name="unions"
    )
    name = models.CharField(_("name"), max_length=200)

    def __str__(self):
        return self.name


class Word(BaseEntity):
    union = models.ForeignKey(Union, on_delete=models.CASCADE, related_name="words")
    name = models.CharField(_("name"), max_length=200)

    def __str__(self):
        return self.name


class Address(BaseEntity):
    user = models.ForeignKey(
        User, verbose_name=_("user"), on_delete=models.CASCADE, related_name="addresses"
    )
    country = models.ForeignKey(
        Country, verbose_name=_("country"), on_delete=models.CASCADE
    )
    division = models.ForeignKey(
        Division, verbose_name=_("division"), on_delete=models.CASCADE
    )
    district = models.ForeignKey(
        District, verbose_name=_("district"), on_delete=models.CASCADE
    )
    sub_district = models.ForeignKey(
        SubDistrict, verbose_name=_("sub district"), on_delete=models.CASCADE
    )
    union = models.ForeignKey(Union, verbose_name=_("union"), on_delete=models.CASCADE)
    word = models.ForeignKey(Word, verbose_name=_("word"), on_delete=models.CASCADE)
    moholla = models.CharField(_("moholla"), max_length=150)
    road_number = models.CharField(_("road number"), max_length=100)
    house_number = models.CharField(_("house number"), max_length=100)

    def __str__(self):
        return self.user.first_name
