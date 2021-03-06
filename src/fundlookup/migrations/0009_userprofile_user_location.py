# Generated by Django 2.2 on 2020-02-07 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundlookup', '0008_remove_userprofile_user_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_location',
            field=models.CharField(choices=[('TN', 'Tamil Nadu'), ('TG', 'Telangana'), ('MP', 'Madhya Pradesh'), ('HR', 'Haryana'), ('CH', 'Chhattisgarh'), ('MR', 'Maharashtra'), ('TR', 'Tripura'), ('KR', 'Karnataka'), ('UP', 'Uttar Pradesh'), ('GJ', 'Gujarat'), ('OD', 'Odisha'), ('RJ', 'Rajasthan'), ('HP', 'Himachal Pradesh')], default='TN', max_length=2),
        ),
    ]
