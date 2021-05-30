# Generated by Django 3.2.3 on 2021-05-20 16:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lead', '0002_lead_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assignedleads', to=settings.AUTH_USER_MODEL),
        ),
    ]
