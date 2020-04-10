# Generated by Django 3.0.5 on 2020-04-10 14:20

from django.db import migrations, models
import django.db.models.deletion
import users.managers


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0003_auto_20200409_1329'),
        ('users', '0002_auto_20200409_2359'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', users.managers.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='state',
            field=models.ForeignKey(blank=True, default=53, help_text='É necessário informar o estado.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='locations.State', verbose_name='Estado'),
        ),
    ]
