# Generated by Django 4.0.5 on 2022-08-08 11:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('emp_rec_management', '0005_remove_employeedetails_user_employeedetails_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeedetails',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='employeedetails',
            name='lname',
        ),
        migrations.AddField(
            model_name='employeedetails',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
