# Generated by Django 3.2.12 on 2022-03-31 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZSSN_Survival', '0005_rename_survivour_id_survivor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survivor',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
