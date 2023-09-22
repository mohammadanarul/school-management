from django.db import models

# from django.contrib.auth import get_user_model
#
# User = get_user_model()


class BaseEntity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # created_by = models.ForeignKey(
    #     User, on_delete=models.SET_NULL, related_name="+", null=True, blank=True
    # )
    # updated_by = models.ForeignKey(
    #     User, on_delete=models.SET_NULL, related_name="+", null=True, blank=True
    # )

    class Meta:
        abstract = True
