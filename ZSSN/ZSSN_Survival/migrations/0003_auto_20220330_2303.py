# Generated by Django 3.2.12 on 2022-03-30 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZSSN_Survival', '0002_alter_survivor_is_infected'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survivor',
            name='gender',
            field=models.CharField(choices=[('0', 'Male'), ('1', 'Female'), ('2', 'Other')], max_length=50),
        ),
        migrations.AlterField(
            model_name='survivor',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='survivor',
            name='is_infected',
            field=models.CharField(choices=[('0', 'Non-Infected'), ('1', 'Infected')], default=0, max_length=50),
        ),
    ]
