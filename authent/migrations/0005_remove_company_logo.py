# Generated by Django 4.2 on 2023-06-05 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authent', '0004_remove_userprofile_company_company_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='logo',
        ),
    ]
