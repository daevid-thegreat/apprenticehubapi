# Generated by Django 4.2 on 2023-06-07 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authent', '0005_remove_company_logo'),
        ('opening', '0006_opening_status_application'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apprentice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('pay', models.CharField(max_length=50)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apprentices', to='authent.company')),
            ],
        ),
    ]
