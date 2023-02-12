# Generated by Django 4.1.6 on 2023-02-09 09:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('published', models.BooleanField()),
                ('number_of_views', models.PositiveBigIntegerField()),
                ('tags', models.ManyToManyField(related_name='posts', to='profiles.technology')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
