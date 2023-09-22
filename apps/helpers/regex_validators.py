from django.core.validators import RegexValidator

phone_number_validator = RegexValidator(
    regex=r"^(((?:\+88)?(?:\d{11}))|((?:01)?(?:\d{11})))$",
    message="Phone number must be entered in the format: +8801555555550, "
    "Up to 11 digits allowed.",
)
