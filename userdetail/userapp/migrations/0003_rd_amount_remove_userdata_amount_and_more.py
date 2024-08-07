# Generated by Django 4.2.7 on 2023-12-08 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_userdata_amount_userdata_interst_amt_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='rd_amount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('noof_year', models.IntegerField()),
                ('interst_amt', models.IntegerField()),
                ('rate_of_interest', models.CharField(max_length=50)),
                ('total_investement', models.BigIntegerField()),
                ('total_returns', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='interst_amt',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='noof_year',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='rate_of_interest',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='total_amount',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='total_investement',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='total_returns',
        ),
    ]
