# Generated by Django 4.0.6 on 2022-07-26 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegionsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regName', models.CharField(max_length=100, verbose_name='region')),
                ('type', models.CharField(max_length=50, verbose_name='type')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='slug')),
            ],
        ),
        migrations.CreateModel(
            name='CitiesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityName', models.CharField(max_length=100, verbose_name='City')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='slug')),
                ('lat', models.FloatField(verbose_name='latitude')),
                ('lon', models.FloatField(verbose_name='longitude')),
                ('reg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weatherforecast.regionsmodel', verbose_name='region')),
            ],
        ),
    ]
