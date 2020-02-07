from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    username            = models.CharField("Name", max_length=120, default="")
    USER_TYPE           = [
        ('VR', "Vendor"),
        ('FD', "Funder"),
        ('PP', "Political Party"),
        ('AD', "Admin")
    ]
    user_type           = models.CharField(
        max_length=2,
        choices=USER_TYPE,
        default="FD",
    )

    USER_LOCATION       = [
        ('TN', "Tamil Nadu"),
        ('TG', "Telangana"),
        ('MP', "Madhya Pradesh"),
        ('HR', "Haryana"),
        ('CH', "Chhattisgarh"),
        ('MR', "Maharashtra"),
        ('TR', "Tripura"),
        ('KR', "Karnataka"),
        ('UP', "Uttar Pradesh"),
        ('GJ', "Gujarat"),
        ('OD', "Odisha"),
        ('RJ', "Rajasthan"),
        ('HP', "Himachal Pradesh"),
    ]

    user_location         = models.CharField(
        max_length=2,
        choices=USER_LOCATION,
        default="TN",
    )

    avatar_path         = models.CharField("Avatar Path", max_length=500)
    metamask_address    = models.CharField("Metamask Address", max_length=500)
    available_funds     = models.FloatField("Available Funds")
    amount_requested    = models.FloatField("Amount Requested")

class Funder(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE)

    FUNDER_TYPE         = [
        ("IND", "Individual"),
        ("ORG", "Organisation"),
    ]
    funder_type         = models.CharField(
        max_length=3,
        choices=FUNDER_TYPE,
        default="IND",
    )

class Vendor(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE)

    VENDOR_TYPE         = [
        ("PB", "Publicity"),
        ("EV", "Event"),
        ("TR", "Travel"),
        ("MC", "Miscellaneous"),
    ]
    vendor_type         = models.CharField(
        max_length=2,
        choices=VENDOR_TYPE,
        default="MC",
    )

class PoliticalParty(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    enabled             = models.BooleanField("Enabled", default=True)
    cap                 = models.FloatField("Cap", default='5000')

    PARTY_TYPE         = [
        ("RG", "Regional"),
        ("NT", "National"),
    ]
    party_type         = models.CharField(
        max_length=2,
        choices=PARTY_TYPE,
        default="NT",
    )

class Admin(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE)


class Transaction(models.Model):
    donated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_donated_by')
    donated_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_donated_to')
    amount     = models.FloatField("Amount")

class Party(models.Model):
    name    = models.CharField("Name", max_length=120)
    address = models.CharField("Address", max_length=500)
    symbol  = models.CharField("Symbol", max_length=500,null=True)

