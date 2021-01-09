# Generated by Django 3.1 on 2020-09-14 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0009_tariffication_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='insurance',
            name='tariffications',
        ),
        migrations.RemoveField(
            model_name='insurancetariffication',
            name='insurance',
        ),
        migrations.AddField(
            model_name='insurancetariffication',
            name='insurer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='insur_tarif_insurerZ', to='insurance.insurer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='insurer',
            name='tariffications',
            field=models.ManyToManyField(related_name='insurer_tariffication', through='insurance.InsuranceTariffication', to='insurance.Tariffication'),
        ),
    ]