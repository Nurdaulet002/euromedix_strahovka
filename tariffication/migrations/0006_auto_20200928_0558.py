# Generated by Django 3.1 on 2020-09-28 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0014_auto_20200928_0500'),
        ('tariffication', '0005_auto_20200928_0543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tariffication',
            name='insurer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tariffications_insurer', to='insurance.insurer'),
        ),
    ]
