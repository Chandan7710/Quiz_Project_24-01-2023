# Generated by Django 4.1.5 on 2023-01-24 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0002_leaderboard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaderboard',
            name='quiz_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz_app.quiz_category'),
        ),
    ]