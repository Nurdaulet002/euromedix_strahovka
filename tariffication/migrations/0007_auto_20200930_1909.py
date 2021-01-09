# Generated by Django 3.1 on 2020-09-30 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tariffication', '0006_auto_20200928_0558'),
    ]

    operations = [
        migrations.AddField(
            model_name='tariffication',
            name='object_copy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children_copy', to='tariffication.tariffication'),
        ),
        migrations.AlterField(
            model_name='tariffication',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='tariffication.tariffication'),
        ),
    ]
