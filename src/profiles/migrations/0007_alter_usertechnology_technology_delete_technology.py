# Generated by Django 4.1.6 on 2023-02-14 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
        ('wall', '0002_alter_post_tags'),
        ('profiles', '0006_remove_usernet_followers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertechnology',
            name='technology',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skills.technology'),
        ),
        migrations.DeleteModel(
            name='Technology',
        ),
    ]
