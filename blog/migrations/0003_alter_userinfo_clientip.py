# Generated by Django 5.0.1 on 2025-02-18 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_userinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='clientip',
            field=models.CharField(max_length=50),
        ),
    ]
