# Generated by Django 4.0.3 on 2023-06-08 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='triaje',
            name='peso',
            field=models.IntegerField(blank=True, help_text='en kg', null=True),
        ),
    ]