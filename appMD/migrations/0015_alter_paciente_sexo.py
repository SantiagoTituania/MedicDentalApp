# Generated by Django 4.1.3 on 2023-02-27 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMD', '0014_alter_paciente_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='sexo',
            field=models.IntegerField(choices=[('M', 'Masculino'), ('F', 'Femenino')], verbose_name='Sexo'),
        ),
    ]