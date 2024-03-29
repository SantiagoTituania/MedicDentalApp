# Generated by Django 4.1.3 on 2023-06-07 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMD', '0018_alter_historia_motivoconsulta'),
    ]

    operations = [
        migrations.AddField(
            model_name='historia',
            name='anestesiaAlergia',
            field=models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=11, null=True, verbose_name='Enfermedad'),
        ),
        migrations.AddField(
            model_name='historia',
            name='antibioticosAlergia',
            field=models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=11, null=True, verbose_name='Enfermedad'),
        ),
        migrations.AddField(
            model_name='historia',
            name='asma',
            field=models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=11, null=True, verbose_name='Enfermedad'),
        ),
        migrations.AddField(
            model_name='historia',
            name='cardiacas',
            field=models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=11, null=True, verbose_name='Enfermedad'),
        ),
        migrations.AddField(
            model_name='historia',
            name='diabetes',
            field=models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=11, null=True, verbose_name='Enfermedad'),
        ),
        migrations.AddField(
            model_name='historia',
            name='hemorragias',
            field=models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=11, null=True, verbose_name='Enfermedad'),
        ),
        migrations.AddField(
            model_name='historia',
            name='otros',
            field=models.TextField(blank=True, max_length=200, verbose_name='Otros'),
        ),
        migrations.AddField(
            model_name='historia',
            name='sida',
            field=models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=11, null=True, verbose_name='Enfermedad'),
        ),
        migrations.AddField(
            model_name='historia',
            name='tuberculosis',
            field=models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=11, null=True, verbose_name='Enfermedad'),
        ),
    ]
