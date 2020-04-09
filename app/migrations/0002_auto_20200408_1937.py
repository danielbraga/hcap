# Generated by Django 3.0.5 on 2020-04-08 19:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_fill_states_and_cities'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='healthcareunity',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='healthcareunity',
            name='email',
        ),
        migrations.RemoveField(
            model_name='healthcareunity',
            name='is_validated',
        ),
        migrations.RemoveField(
            model_name='healthcareunity',
            name='phone',
        ),
        migrations.AddField(
            model_name='healthcareunity',
            name='notifiers',
            field=models.ManyToManyField(related_name='unities', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='healthcareunity',
            name='municipality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='healthcare_unities', to='locations.Municipality', verbose_name='Município'),
        ),
    ]