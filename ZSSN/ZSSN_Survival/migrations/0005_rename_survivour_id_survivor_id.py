# Generated by Django 3.2.12 on 2022-03-30 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ZSSN_Survival', '0004_auto_20220330_2311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='survivor',
            old_name='survivour_id',
            new_name='id',
        ),
    ]
