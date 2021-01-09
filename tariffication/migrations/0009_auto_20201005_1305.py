# Generated by Django 3.1 on 2020-10-05 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0019_delete_harm'),
        ('tariffication', '0008_auto_20200930_1910'),
    ]

    operations = [
        migrations.CreateModel(
            name='Harm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, null=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'harms',
            },
        ),
        migrations.CreateModel(
            name='ProfessionHarm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('harm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='harm_rel', to='tariffication.harm')),
                ('insurance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='insurance_rel', to='insurance.insurance')),
                ('insurer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='insurer_rel', to='insurance.insurer')),
                ('profession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profession_rel', to='insurance.profession')),
            ],
            options={
                'db_table': 'profession_harm',
            },
        ),
        migrations.AddField(
            model_name='harm',
            name='professions',
            field=models.ManyToManyField(through='tariffication.ProfessionHarm', to='insurance.Profession'),
        ),
    ]
