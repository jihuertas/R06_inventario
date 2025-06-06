# Generated by Django 5.1.3 on 2025-04-24 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=250)),
                ('stock', models.IntegerField(default=0)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
            options={
                'verbose_name_plural': 'Productos',
            },
        ),
    ]
