# Generated by Django 5.0.4 on 2024-04-11 04:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0003_profile_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Department', models.CharField(choices=[('SAC', 'SAC'), ('Engineering', 'Engineering'), ('SAP_SD', 'SAP_SD'), ('SAP_PP', 'SAP_PP'), ('SAP_MM', 'SAP_MM'), ('SAP_FICO', 'SAP_FICO'), ('SAP_ABAP', 'SAP_ABAP')], max_length=50)),
                ('Position', models.CharField(choices=[('Trainee', 'Trainee'), ('Associate', 'Associate'), ('Consultant', 'Consultant'), ('Senior Associate', 'Senior Associate'), ('Manager', 'Manager')], max_length=50)),
                ('Date', models.DateTimeField()),
                ('Requesttype', models.CharField(choices=[('Hardware', 'Hardware'), ('Software', 'Software'), ('Network Connectivity', 'Network Connectivity'), ('Technical_Support', 'Technical_Support'), ('Comaplaints', 'Complaints')], max_length=50)),
                ('Manufacturer', models.TextField()),
                ('Issue_Title', models.TextField()),
                ('Description', models.TextField()),
                ('Asset', models.IntegerField()),
                ('Status', models.CharField(choices=[('Register', 'Register'), ('Assigned', 'Assigned'), ('Request_fulfiled', 'Request_fulfiled'), ('Aborted', 'Aborted'), ('Closed', 'Closed')], max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modify', models.DateTimeField(auto_now=True, null=True)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ServiceRequest', to='profiles.profile')),
            ],
        ),
    ]
