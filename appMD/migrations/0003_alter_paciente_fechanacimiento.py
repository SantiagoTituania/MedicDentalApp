# Generated by Django 4.1.3 on 2023-01-21 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMD', '0002_paciente_correo_alter_paciente_fechanacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='fechaNacimiento',
            field=models.DateField(),
        ),
    ]