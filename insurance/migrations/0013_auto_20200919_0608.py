# Generated by Django 3.1 on 2020-09-19 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0012_auto_20200914_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='insurancedrug',
            name='drug',
        ),
        migrations.RemoveField(
            model_name='insurancedrug',
            name='insurer',
        ),
        migrations.RemoveField(
            model_name='insurancetariffication',
            name='insurer',
        ),
        migrations.RemoveField(
            model_name='insurancetariffication',
            name='tariffication',
        ),
        migrations.RemoveField(
            model_name='insurercompulsorypackage',
            name='compulsory_package',
        ),
        migrations.RemoveField(
            model_name='insurercompulsorypackage',
            name='insurance',
        ),
        migrations.RemoveField(
            model_name='insurercompulsorypackage',
            name='insurer',
        ),
        migrations.RemoveField(
            model_name='insurer',
            name='compulsory_packages',
        ),
        migrations.RemoveField(
            model_name='insurer',
            name='drugs',
        ),
        migrations.RemoveField(
            model_name='insurer',
            name='tariffications',
        ),
        migrations.RemoveField(
            model_name='personification',
            name='compulsory_package',
        ),
        migrations.DeleteModel(
            name='CompulsoryPackage',
        ),
        migrations.DeleteModel(
            name='Drug',
        ),
        migrations.DeleteModel(
            name='InsuranceDrug',
        ),
        migrations.DeleteModel(
            name='InsuranceTariffication',
        ),
        migrations.DeleteModel(
            name='InsurerCompulsoryPackage',
        ),
        migrations.DeleteModel(
            name='Tariffication',
        ),
    ]
