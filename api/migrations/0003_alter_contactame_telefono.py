# Generated by Django 3.2.4 on 2023-11-24 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20231124_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactame',
            name='telefono',
            field=models.IntegerField(max_length=11),
        ),
    ]
