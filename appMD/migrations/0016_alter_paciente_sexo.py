# Generated by Django 4.1.3 on 2023-02-27 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMD', '0015_alter_paciente_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=11, verbose_name='Sexo'),
        ),
    ]
