# Generated by Django 4.2.5 on 2023-11-28 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('talleres', '0006_rename_instructores_instructore_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tallere',
            name='inscripcion',
        ),
    ]