# Generated by Django 2.2 on 2019-08-18 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundlookup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='symbol',
            field=models.CharField(max_length=500, null=True, verbose_name='Symbol'),
        ),
        migrations.AlterField(
            model_name='party',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Name'),
        ),
    ]