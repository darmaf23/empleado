# Generated by Django 4.0.4 on 2022-04-30 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='empleado'),
        ),
    ]
