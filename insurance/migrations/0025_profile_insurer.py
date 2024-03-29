# Generated by Django 3.1 on 2020-12-06 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0024_insurer_profession'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='insurer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='profiles_insurer', to='insurance.insurer'),
            preserve_default=False,
        ),
    ]
