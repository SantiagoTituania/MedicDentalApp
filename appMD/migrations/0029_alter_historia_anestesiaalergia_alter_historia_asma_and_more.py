# Generated by Django 4.1.3 on 2023-06-08 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMD', '0028_alter_historia_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historia',
            name='anestesiaAlergia',
            field=models.CharField(blank=True, choices=[('S', 'Si'), ('N', 'No')], max_length=11, null=True, verbose_name='Alergia anestesia'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='asma',
            field=models.CharField(blank=True, choices=[('S', 'Si'), ('N', 'No')], max_length=11, null=True, verbose_name='Asma'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='atm',
            field=models.CharField(blank=True, choices=[('B', 'Bueno'), ('M', 'Malo')], max_length=11, null=True, verbose_name='A.T.M.'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='cardiacas',
            field=models.CharField(blank=True, choices=[('S', 'Si'), ('N', 'No')], max_length=11, null=True, verbose_name='Enfermedad cardiacas'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='carrillo',
            field=models.CharField(blank=True, choices=[('B', 'Bueno'), ('M', 'Malo')], max_length=11, null=True, verbose_name='Carrillo'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='diabetes',
            field=models.CharField(blank=True, choices=[('S', 'Si'), ('N', 'No')], max_length=11, null=True, verbose_name='Diabetes'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='fechaTratamiento1',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historia',
            name='fechaTratamiento2',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historia',
            name='fechaTratamiento3',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historia',
            name='fechaTratamiento4',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historia',
            name='frecuenciaCardiaca',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Frecuencia Cardiaca'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='frecuenciaRespiratoria',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Frecuencia respiratoria'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='ganglios',
            field=models.CharField(blank=True, choices=[('B', 'Bueno'), ('M', 'Malo')], max_length=11, null=True, verbose_name='Ganglios'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='glandulasSalivales',
            field=models.CharField(blank=True, choices=[('B', 'Bueno'), ('M', 'Malo')], max_length=11, null=True, verbose_name='Glándulas salivales'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='hemorragias',
            field=models.CharField(blank=True, choices=[('S', 'Si'), ('N', 'No')], max_length=11, null=True, verbose_name='Hemorrágias'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='hipertension',
            field=models.CharField(blank=True, choices=[('S', 'Si'), ('N', 'No')], max_length=11, null=True, verbose_name='Hipertensión'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='labios',
            field=models.CharField(blank=True, choices=[('B', 'Bueno'), ('M', 'Malo')], max_length=11, null=True, verbose_name='Labios'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='lengua',
            field=models.CharField(blank=True, choices=[('B', 'Bueno'), ('M', 'Malo')], max_length=11, null=True, verbose_name='Lengua'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='maxilarInferior',
            field=models.CharField(blank=True, choices=[('B', 'Bueno'), ('M', 'Malo')], max_length=11, null=True, verbose_name='Maxilar Inferior'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='maxilarSuperior',
            field=models.CharField(blank=True, choices=[('B', 'Bueno'), ('M', 'Malo')], max_length=11, null=True, verbose_name='Maxilar superior'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='mejillas',
            field=models.CharField(blank=True, choices=[('B', 'Bueno'), ('M', 'Malo')], max_length=11, null=True, verbose_name='Mejillas'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='orofaringe',
            field=models.CharField(blank=True, choices=[('B', 'Bueno'), ('M', 'Malo')], max_length=11, null=True, verbose_name='Orofaringe'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='paladar',
            field=models.CharField(blank=True, choices=[('B', 'Bueno'), ('M', 'Malo')], max_length=11, null=True, verbose_name='Paladar'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='piso',
            field=models.CharField(blank=True, choices=[('B', 'Bueno'), ('M', 'Malo')], max_length=11, null=True, verbose_name='Piso'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='presionArterial',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Presión Arterial'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='sida',
            field=models.CharField(blank=True, choices=[('S', 'Si'), ('N', 'No')], max_length=11, null=True, verbose_name='VIH/SIDA'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='temperatura',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Temperatura'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='tuberculosis',
            field=models.CharField(blank=True, choices=[('S', 'Si'), ('N', 'No')], max_length=11, null=True, verbose_name='Tuberculosis'),
        ),
    ]