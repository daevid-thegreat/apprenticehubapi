# Generated by Django 4.2 on 2023-06-08 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opening', '0009_apprentice_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='apprentice',
            name='email',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]