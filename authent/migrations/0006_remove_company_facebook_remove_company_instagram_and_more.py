# Generated by Django 4.2 on 2023-06-08 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authent', '0005_remove_company_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='company',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='company',
            name='linkedin',
        ),
        migrations.RemoveField(
            model_name='company',
            name='twitter',
        ),
    ]
