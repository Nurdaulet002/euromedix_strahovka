# Generated by Django 3.1 on 2020-10-05 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prof_med_exam', '0003_auto_20201005_1239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professionharm',
            name='harm',
        ),
        migrations.RemoveField(
            model_name='professionharm',
            name='insurance',
        ),
        migrations.RemoveField(
            model_name='professionharm',
            name='insurer',
        ),
        migrations.RemoveField(
            model_name='professionharm',
            name='profession',
        ),
        migrations.DeleteModel(
            name='Harm',
        ),
        migrations.DeleteModel(
            name='ProfessionHarm',
        ),
    ]