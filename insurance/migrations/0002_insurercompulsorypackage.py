# Generated by Django 3.1 on 2020-08-17 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InsurerCompulsoryPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compulsory_package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_compul_pack', to='insurance.compulsorypackage')),
                ('insurer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_insurer', to='insurance.insurer')),
            ],
            options={
                'db_table': 'insurer_compulsory_package',
            },
        ),
    ]