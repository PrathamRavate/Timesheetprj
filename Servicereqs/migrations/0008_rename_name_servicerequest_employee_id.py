# Generated by Django 5.0.4 on 2024-04-11 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Servicereqs', '0007_rename_employee_servicerequest_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicerequest',
            old_name='name',
            new_name='employee_id',
        ),
    ]
