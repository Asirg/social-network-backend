# Generated by Django 4.1.6 on 2023-02-10 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0009_alter_commentreaction_emotion_and_more'),
        ('social', '0003_remove_reactionemotion_icon'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ReactionEmotion',
        ),
    ]