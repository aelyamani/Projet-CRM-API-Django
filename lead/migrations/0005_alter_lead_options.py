# Generated by Django 4.0.3 on 2022-04-17 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0004_alter_lead_priority'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lead',
            options={'verbose_name': 'Lead', 'verbose_name_plural': 'Leads'},
        ),
    ]
