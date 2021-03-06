# Generated by Django 4.0.4 on 2022-05-09 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick', models.CharField(max_length=20)),
                ('user_id', models.IntegerField(default=None, null=True)),
                ('user_avatar', models.CharField(max_length=100)),
                ('cover_url', models.CharField(max_length=200)),
                ('last_login', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PlayerVote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('osu_id', models.IntegerField()),
                ('nick', models.CharField(max_length=20)),
                ('avatar_url', models.CharField(max_length=200)),
                ('points', models.IntegerField()),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votes.player')),
            ],
        ),
    ]
