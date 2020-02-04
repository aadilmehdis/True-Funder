from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user                = models.OneToOneField(User, on_delete=models.CASCADE)

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

    avatar_path         = models.CharField("Avatar Path", max_length=500)
    metamask_address    = models.CharField("Metamask Address", max_length=500)
    available_funds     = models.FloatField("Available Funds")
    amount_requested    = models.FloatField("Amount Requested")

class Funder(models.Model):
    user                = models.OneToOneField(User, on_delete=models.CASCADE)

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
    user                = models.OneToOneField(User, on_delete=models.CASCADE)

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
    user                = models.OneToOneField(User, on_delete=models.CASCADE)

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
    user                = models.OneToOneField(User, on_delete=models.CASCADE)


class Transactions(models.Model):
    donated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_donated_by')
    donated_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_donated_to')

class Party(models.Model):
    name    = models.CharField("Name", max_length=120)
    address = models.CharField("Address", max_length=500)
    symbol  = models.CharField("Symbol", max_length=500,null=True)

