# Generated by Django 3.1 on 2020-08-17 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, null=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('title_short', models.CharField(max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, null=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'cities',
            },
        ),
        migrations.CreateModel(
            name='CompulsoryPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, null=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'compulsory_packages',
            },
        ),
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, null=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'drugs',
            },
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, null=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('bin', models.CharField(max_length=12, null=True)),
                ('address', models.CharField(max_length=500, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone', models.CharField(max_length=70, null=True)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='insurance_bank', to='insurance.bank')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='insurance_city', to='insurance.city')),
            ],
            options={
                'db_table': 'insurance',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, null=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'regions',
            },
        ),
        migrations.CreateModel(
            name='Tariffication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, null=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('code', models.CharField(max_length=80, null=True)),
                ('parent', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'tariffications',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to='auth.user')),
                ('insurance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profiles_insurance', to='insurance.insurance')),
            ],
            options={
                'db_table': 'profile',
            },
        ),
        migrations.CreateModel(
            name='Insurer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, null=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('bin', models.CharField(max_length=12, null=True)),
                ('address', models.CharField(max_length=500, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone', models.CharField(max_length=70, null=True)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='insurer_bank', to='insurance.bank')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='insurer_city', to='insurance.city')),
            ],
            options={
                'db_table': 'insurers',
            },
        ),
        migrations.CreateModel(
            name='InsuranceTariffication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('omo_price', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('opmo_price', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('insurance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_insurance', to='insurance.insurance')),
                ('tariffication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_tariffication', to='insurance.tariffication')),
            ],
            options={
                'db_table': 'insurance_tariffication',
            },
        ),
        migrations.CreateModel(
            name='InsuranceDrug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_drug', to='insurance.drug')),
                ('insurance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_insurance_drug', to='insurance.insurance')),
            ],
            options={
                'db_table': 'insurance_drug',
            },
        ),
        migrations.AddField(
            model_name='insurance',
            name='drugs',
            field=models.ManyToManyField(related_name='insurance_drug', through='insurance.InsuranceDrug', to='insurance.Drug'),
        ),
        migrations.AddField(
            model_name='insurance',
            name='insurers',
            field=models.ManyToManyField(to='insurance.Insurer'),
        ),
        migrations.AddField(
            model_name='insurance',
            name='tariffications',
            field=models.ManyToManyField(related_name='insurance_tariffication', through='insurance.InsuranceTariffication', to='insurance.Tariffication'),
        ),
        migrations.AddField(
            model_name='city',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities_region', to='insurance.region'),
        ),
        migrations.AddField(
            model_name='bank',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities_bank', to='insurance.city'),
        ),
    ]
