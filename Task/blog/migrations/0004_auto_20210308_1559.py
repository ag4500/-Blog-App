# Generated by Django 3.1.3 on 2021-03-08 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210307_2203'),
    ]

    operations = [
        migrations.DeleteModel(
            name='public',
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.CharField(default='ram', max_length=12),
        ),
    ]
