# Generated by Django 2.2.6 on 2021-07-14 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface_app', '0005_runtask'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='days',
            field=models.IntegerField(default=0, null=True, verbose_name='days'),
        ),
        migrations.AddField(
            model_name='task',
            name='hours',
            field=models.IntegerField(default=0, null=True, verbose_name='hour'),
        ),
        migrations.AddField(
            model_name='task',
            name='interval_switch',
            field=models.BooleanField(default=False, verbose_name='interval_switch'),
        ),
        migrations.AddField(
            model_name='task',
            name='minutes',
            field=models.IntegerField(default=0, null=True, verbose_name='minutes'),
        ),
        migrations.AddField(
            model_name='task',
            name='start_time',
            field=models.DateTimeField(default=None, null=True, verbose_name='start_time'),
        ),
    ]
