# Generated by Django 4.0.6 on 2022-08-31 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_podcast_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('episode', models.CharField(max_length=150)),
                ('podcast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.podcast')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]