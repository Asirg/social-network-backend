# Generated by Django 4.1.6 on 2023-02-11 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_usernet_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='usernet',
            name='activity_status_is_hidden',
            field=models.CharField(choices=[('all', 'all'), ('confirmed', 'confirmed'), ('nobody', 'nobody')], default='all', max_length=20),
        ),
        migrations.AddField(
            model_name='usernet',
            name='chat_is_closed',
            field=models.CharField(choices=[('all', 'all'), ('confirmed', 'confirmed'), ('nobody', 'nobody')], default='all', max_length=20),
        ),
        migrations.AddField(
            model_name='usernet',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usernet',
            name='country',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='usernet',
            name='user_is_hiden',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='follower',
            name='relation',
            field=models.CharField(choices=[('not confirmed', 'not confirmed'), ('confirmed', 'confirmed'), ('blacklist', 'blacklist')], default='not confirmed', max_length=20),
        ),
    ]
