# Generated by Django 3.2 on 2021-04-27 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_property_form_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='form_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
