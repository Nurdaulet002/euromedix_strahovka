# Generated by Django 3.1 on 2020-12-02 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0021_personification_birthdate'),
        ('tariffication', '0021_auto_20201020_0537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='insurance',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='insurance.insurance'),
        ),
    ]