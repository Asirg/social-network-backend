# Generated by Django 4.1.6 on 2023-02-14 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_privacysettings_hidden_fields'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='description',
        ),
        migrations.AddField(
            model_name='usernet',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]