# Generated by Django 5.0.1 on 2025-02-20 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_userinfo_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='clientdata',
            field=models.TextField(blank=True, null=True),
        ),
    ]
