# Generated by Django 3.1 on 2020-10-13 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tariffication', '0014_auto_20201009_0739'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, null=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
