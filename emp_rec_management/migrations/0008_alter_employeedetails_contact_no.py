# Generated by Django 4.0.5 on 2022-08-09 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_rec_management', '0007_remove_employeedetails_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedetails',
            name='contact_no',
            field=models.IntegerField(max_length=10, null=True),
        ),
    ]