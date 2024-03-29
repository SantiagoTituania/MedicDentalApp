# Generated by Django 4.1.3 on 2023-06-07 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMD', '0020_historia_atm_historia_carrillo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historia',
            old_name='glándulasSalivales',
            new_name='glandulasSalivales',
        ),
        migrations.AlterField(
            model_name='historia',
            name='anestesiaAlergia',
            field=models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=11, null=True, verbose_name='Alergia anestesia'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='antibioticosAlergia',
            field=models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=11, null=True, verbose_name='Alergia antibióticos'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='asma',
            field=models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=11, null=True, verbose_name='Asma'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='cardiacas',
            field=models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=11, null=True, verbose_name='Enfermedad cardiacas'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='desTratamiento1',
            field=models.CharField(blank=True, max_length=200, verbose_name='Descripcion tratamient 1'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='desTratamiento10',
            field=models.CharField(blank=True, max_length=200, verbose_name='Descripcion tratamient 10'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='desTratamiento11',
            field=models.CharField(blank=True, max_length=200, verbose_name='Descripcion tratamient 11'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='desTratamiento12',
            field=models.CharField(blank=True, max_length=200, verbose_name='Descripcion tratamient 12'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='desTratamiento2',
            field=models.CharField(blank=True, max_length=200, verbose_name='Descripcion tratamient 2'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='desTratamiento3',
            field=models.CharField(blank=True, max_length=200, verbose_name='Descripcion tratamient 3'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='desTratamiento4',
            field=models.CharField(blank=True, max_length=200, verbose_name='Descripcion tratamient 4'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='desTratamiento5',
            field=models.CharField(blank=True, max_length=200, verbose_name='Descripcion tratamient 5'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='desTratamiento6',
            field=models.CharField(blank=True, max_length=200, verbose_name='Descripcion tratamient 6'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='desTratamiento7',
            field=models.CharField(blank=True, max_length=200, verbose_name='Descripcion tratamient 7'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='desTratamiento8',
            field=models.CharField(blank=True, max_length=200, verbose_name='Descripcion tratamient 8'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='desTratamiento9',
            field=models.CharField(blank=True, max_length=200, verbose_name='Descripcion tratamient 9'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='diabetes',
            field=models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=11, null=True, verbose_name='Diabetes'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='hemorragias',
            field=models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=11, null=True, verbose_name='Hemorrágias'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='sida',
            field=models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=11, null=True, verbose_name='VIH/SIDA'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='tuberculosis',
            field=models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=11, null=True, verbose_name='Tuberculosis'),
        ),
    ]
