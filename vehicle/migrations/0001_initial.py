# Generated by Django 3.2.8 on 2021-10-30 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicletype', models.CharField(max_length=100)),
                ('modelname', models.CharField(max_length=100)),
                ('vehiclecolor', models.CharField(max_length=100)),
                ('enginetype', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='media')),
            ],
        ),
    ]
