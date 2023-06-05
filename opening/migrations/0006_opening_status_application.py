# Generated by Django 4.2 on 2023-06-05 15:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opening', '0005_remove_opening_requirements'),
    ]

    operations = [
        migrations.AddField(
            model_name='opening',
            name='status',
            field=models.CharField(default='open', max_length=50),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('email', models.CharField(max_length=50)),
                ('education', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=300)),
                ('status', models.CharField(default='pending', max_length=50)),
                ('opening', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opening.opening')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
