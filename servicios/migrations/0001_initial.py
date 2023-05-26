# Generated by Django 4.0.3 on 2023-05-26 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('activo', models.BooleanField(default=True, editable=False)),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('precio', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'servicios',
                'verbose_name_plural': 'servicios',
            },
        ),
    ]
