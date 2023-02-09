# Generated by Django 4.1.6 on 2023-02-09 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0005_alter_commentreaction_comment_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcomment',
            old_name='create_date',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='postcomment',
            old_name='update_date',
            new_name='updated_date',
        ),
        migrations.AlterField(
            model_name='post',
            name='number_of_views',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]