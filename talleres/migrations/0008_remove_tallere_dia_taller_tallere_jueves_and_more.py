# Generated by Django 4.2.5 on 2023-11-28 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talleres', '0007_remove_tallere_inscripcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tallere',
            name='dia_taller',
        ),
        migrations.AddField(
            model_name='tallere',
            name='jueves',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='tallere',
            name='lunes',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='tallere',
            name='martes',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='tallere',
            name='miercoles',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='tallere',
            name='sabado',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='tallere',
            name='viernes',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
