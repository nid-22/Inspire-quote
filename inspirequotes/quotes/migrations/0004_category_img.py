# Generated by Django 3.1.7 on 2021-02-20 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_auto_20210220_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='img',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]