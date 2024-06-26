# Generated by Django 4.1.5 on 2024-02-28 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corecode', '0019_alter_gen_dt_currency_currencynumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gen_DT_CBR_Rates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateCBR', models.DateField()),
                ('RateUSD', models.CharField(max_length=200)),
                ('RateEUR', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['RateEUR'],
            },
        ),
    ]
