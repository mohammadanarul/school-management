from django.db import models
from django.utils.translation import gettext_lazy as _


class InstituteTypes(models.IntegerChoices):
    PRIMARY = 1, _("Primary")
    SECONDARY = 2, _("Secondary")


class UserRoles(models.IntegerChoices):
    ADMIN = 1, _("Admin")
    STUDENT = 2, _("Student")
    HEAD_TEACHER = 3, _("Head Teacher")
    HEAD_ASSISTANT_HEAD_TEACHER = 4, _("Assistant Head Teacher")
    ASSISTANT_HEAD_TEACHER = 5, _("Assistant Teacher")
    STAFF = 6, _("Staff")


class Genders(models.IntegerChoices):
    MALE = 1, _("Male")
    FEMALE = 2, _("Female")
    OTHERS = 3, _("Others")


class BloodGroups(models.IntegerChoices):
    A_PLUS = 1, _("A+")
    A_MINUS = 2, _("A-")
    B_PLUS = 3, _("B+")
    B_MINUS = 4, _("B-")
    O_PLUS = 5, _("O+")
    AB_PLUS = 6, _("AB+")
    AB_MINUS = 7, _("AB-")


class SalaryGrade(models.IntegerChoices):
    FIRST_GRADE = 1, _("1st grade")
    SECOND_GRADE = 2, _("2nd grade")
    THIRD_GRADE = 3, _("3rd grade")
    FOUR_GRADE = 5, _("5th grade")
    SIX_GRADE = 6, _("6th grade")
    NINE_GRADE = 9, _("9th grade")
    TEEN_GRADE = 10, _("10th grade")
    ELEVEN_GRADE = 11, _("11th grade")
    TWELVE_GRADE = 12, _("12th grade")
    THIRTEEN_GRADE = 13, _("13th grade")
    FOURTEEN_GRADE = 14, _("14th grade")
    FIFTEEN_GRADE = 15, _("15th grade")
    SIXTEEN_GRADE = 16, _("16th grade")
    SEVEN_GRADE = 17, _("17th grade")
    EIGHTEEN_GRADE = 18, _("18th grade")
    NINETEEN_GRADE = 19, _("19th grade")
    TWENTY_GRADE = 20, _("20th grade")


class CertificateType(models.IntegerChoices):
    PEC = 1, _("PEC")
    JSC = 2, _("JSC")
    SSC = 3, _("SSC")
    HSC = 4, _("HSC")
    BA = 5, _("BA (Hons)")
    BSC = 6, _("BSC (Hons)")
    BBA = 7, _("BBA")
    MBA = 8, _("MBA")


class SubjectType(models.IntegerChoices):
    MANDATORY = 1, _("MANDATORY")
    OPTIONAL = 2, _("OPTIONAL")


class ExamType(models.IntegerChoices):
    FIRST_ANNIVERSARY = 1, _("1st Anniversary")
    SECOND_ANNIVERSARY = 2, _("2nd Anniversary")
    THIRD_ANNIVERSARY = 3, _("3rd Anniversary")
    TEST_ANNIVERSARY = 4, _("TEST Exam")


class ExamStatus(models.IntegerChoices):
    ACTIVE = 1, "Active"
    EXPIRED = 2, "Expired"


class FeeTypes(models.IntegerChoices):
    EXAM = 1, "Exam"
    EVENT = 2, "Event"
    MONTHLY = 3, "Monthly"
    YEARLY = 4, "Yearly"


class FeeStatus(models.IntegerChoices):
    PAID = 1, "Active"
    DUE = 2, "Expired"


class AttendanceType(models.IntegerChoices):
    PRESENT = 1, "PRESENT"
    ABSENT = 2, "ABSENT"
