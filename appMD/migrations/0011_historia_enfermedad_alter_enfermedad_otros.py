# Generated by Django 4.1.3 on 2023-01-23 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appMD', '0010_enfermedad_alter_historia_paciente'),
    ]

    operations = [
        migrations.AddField(
            model_name='historia',
            name='enfermedad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appMD.enfermedad', verbose_name='Enfermedad'),
        ),
        migrations.AlterField(
            model_name='enfermedad',
            name='otros',
            field=models.TextField(max_length=200, verbose_name='Otros'),
        ),
    ]
