# Generated by Django 4.1.3 on 2022-11-30 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('rutcliente', models.CharField(db_column='rutCliente', max_length=45, primary_key=True, serialize=False)),
                ('nombrecliente', models.CharField(blank=True, db_column='nombreCliente', max_length=45, null=True)),
                ('apellidocliente', models.CharField(blank=True, db_column='apellidoCliente', max_length=45, null=True)),
                ('correocliente', models.CharField(blank=True, db_column='correoCliente', max_length=45, null=True)),
                ('mensajecliente', models.CharField(blank=True, db_column='mensajeCliente', max_length=10000, null=True)),
            ],
            options={
                'db_table': 'formulario',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Rol',
        ),
    ]
