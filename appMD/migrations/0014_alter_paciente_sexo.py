# Generated by Django 4.1.3 on 2023-02-27 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMD', '0013_rename_rdv_cita'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='sexo',
            field=models.IntegerField(choices=[(1, 'Masculino'), (2, 'Femenino')], verbose_name='Sexo'),
        ),
    ]