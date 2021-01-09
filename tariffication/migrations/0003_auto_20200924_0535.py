# Generated by Django 3.1 on 2020-09-24 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('insurance', '0013_auto_20200919_0608'),
        ('tariffication', '0002_auto_20200919_0610'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, null=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'service_groups',
            },
        ),
        migrations.RemoveField(
            model_name='service',
            name='insurance',
        ),
        migrations.CreateModel(
            name='Tariffication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('insurance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tariffications_insurance', to='insurance.insurance')),
                ('insurer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tariffications_insurer', to='insurance.insurer')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tariffication.tariffication')),
            ],
            options={
                'db_table': 'tariffication',
            },
        ),
    ]