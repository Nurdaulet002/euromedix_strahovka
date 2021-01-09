# Generated by Django 3.1 on 2020-08-17 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0002_insurercompulsorypackage'),
    ]

    operations = [
        migrations.AddField(
            model_name='insurer',
            name='compulsory_packages',
            field=models.ManyToManyField(related_name='insurer_compulsory_packages', through='insurance.InsurerCompulsoryPackage', to='insurance.CompulsoryPackage'),
        ),
    ]
