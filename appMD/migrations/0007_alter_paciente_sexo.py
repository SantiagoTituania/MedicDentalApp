# Generated by Django 4.1.3 on 2023-01-22 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMD', '0006_alter_usuario_rol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='sexo',
            field=models.IntegerField(choices=[(1, 'Masculino'), (2, 'Femenino')], default=1, verbose_name='Sexo'),
        ),
    ]
