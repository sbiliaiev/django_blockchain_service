# Generated by Django 2.0.6 on 2018-06-09 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deviceId', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='DeviceData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('rvc_as', models.TextField()),
                ('ctx_era', models.TextField()),
                ('cnt', models.FloatField()),
                ('mix_stp', models.IntegerField()),
                ('mux_delta_vp', models.FloatField()),
                ('coef_ttx', models.FloatField()),
                ('active', models.BooleanField()),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.Device')),
            ],
        ),
    ]
