# Generated by Django 5.0.4 on 2024-04-11 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Servicereqs', '0009_rename_employee_id_servicerequest_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerequest',
            name='employee_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
