# Generated by Django 4.1.3 on 2023-01-22 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMD', '0005_usuario_contrasenia_usuario_nusuario_usuario_rol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.IntegerField(choices=[(1, 'Admininistrador'), (2, 'Médico'), (3, 'Asistente')], default=1, verbose_name='Rol'),
        ),
    ]