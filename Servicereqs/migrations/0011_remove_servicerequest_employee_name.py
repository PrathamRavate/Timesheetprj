# Generated by Django 5.0.4 on 2024-04-11 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Servicereqs', '0010_servicerequest_employee_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicerequest',
            name='employee_name',
        ),
    ]
