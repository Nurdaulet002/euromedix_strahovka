# Generated by Django 3.1 on 2020-10-05 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0017_profession'),
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
    ]