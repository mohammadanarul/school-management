from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()


class EmailOrPhoneNumberBackend(ModelBackend):
    def authenticate(self, request, mobile_number=None, password=None, **kwargs):
        try:
            user = User.objects.get(
                Q(mobile_number__iexact=mobile_number) | Q(email__iexact=mobile_number)
            )
        except User.DoesNotExist:
            User().set_password(password)
            return
        except User.MultipleObjectsReturned:
            user = (
                User.objects.filter(
                    Q(mobile_number__iexact=mobile_number)
                    | Q(email__iexact=mobile_number)
                )
                .order_by("id")
                .first()
            )

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
