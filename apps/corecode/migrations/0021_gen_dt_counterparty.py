# Generated by Django 4.1.5 on 2024-02-28 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corecode', '0020_gen_dt_cbr_rates'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gen_DT_CounterParty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CounterPartyID_1C', models.CharField(max_length=100)),
                ('CounterPartyEN', models.CharField(max_length=200)),
                ('CounterPartyRU', models.CharField(max_length=200)),
                ('CounterPartyTR', models.CharField(max_length=200)),
                ('CounterPartyINN', models.CharField(max_length=200)),
                ('CounterPartyKPP', models.CharField(max_length=200)),
                ('Client', models.BooleanField(default=False)),
                ('ClientGroup', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['CounterPartyEN'],
            },
        ),
    ]
