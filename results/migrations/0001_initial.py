# Generated by Django 3.2.2 on 2021-05-14 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('constructors', '0001_initial'),
        ('statuses', '0001_initial'),
        ('drivers', '0001_initial'),
        ('races', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='races.race')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='drivers.driver')),
                ('constructor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='constructors.constructor')),
                ('number', models.IntegerField(null=True)),
                ('grid', models.IntegerField()),
                ('position', models.IntegerField(null=True)),
                ('position_text', models.CharField(max_length=255)),
                ('position_order', models.IntegerField()),
                ('points', models.FloatField()),
                ('laps', models.IntegerField()),
                ('time', models.CharField(max_length=255, null=True)),
                ('milliseconds', models.FloatField(null=True)),
                ('fastest_lap', models.IntegerField(null=True)),
                ('rank', models.IntegerField(null=True)),
                ('fastest_lap_time', models.CharField(max_length=255, null=True)),
                ('fastest_lap_speed', models.CharField(max_length=255, null=True)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='statuses.status')),
            ],
        ),
    ]
