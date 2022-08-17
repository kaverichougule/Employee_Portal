# Generated by Django 4.0.5 on 2022-08-07 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_rec_management', '0004_rename_emp_details_employeedetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeedetails',
            name='user',
        ),
        migrations.AddField(
            model_name='employeedetails',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employeedetails',
            name='fname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employeedetails',
            name='lname',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
