# Generated by Django 3.1 on 2020-09-08 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0008_personification_compulsory_package'),
    ]

    operations = [
        migrations.AddField(
            model_name='tariffication',
            name='code',
            field=models.CharField(max_length=80, null=True),
        ),
    ]