# Generated by Django 4.1.3 on 2023-02-02 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appMD', '0012_remove_historia_enfermedad_rdv'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Rdv',
            new_name='Cita',
        ),
    ]
