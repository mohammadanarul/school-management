from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.helpers.models import BaseEntity
from apps.institutes.models import Institute


class Library(BaseEntity):
    institute = models.OneToOneField(
        Institute, verbose_name=_("institute"), on_delete=models.CASCADE
    )
    name = models.CharField(_("name"), max_length=255)
    established_date = models.DateField(_("established date"))


class Book(BaseEntity):
    library = models.ForeignKey(
        Library,
        verbose_name=_("library"),
        on_delete=models.CASCADE,
        related_name="books",
    )
    writer_name = models.CharField(_("writer_name"), max_length=255)
    name = models.CharField(_("writer_name"), max_length=255)
    cover_image = models.ImageField(
        _("cover_image"), upload_to="library/books/cover-images/"
    )
    pdf_file = models.FileField(_("pdf file"), upload_to="library/books/pdfs/")
    page_number = models.CharField(_("page number"), max_length=20)
    publication = models.CharField(_("publication"), max_length=250)

    def __str__(self):
        return self.name
