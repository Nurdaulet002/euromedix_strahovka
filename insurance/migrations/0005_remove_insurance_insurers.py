# Generated by Django 3.1 on 2020-09-02 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0004_insurercompulsorypackage_insurance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='insurance',
            name='insurers',
        ),
    ]