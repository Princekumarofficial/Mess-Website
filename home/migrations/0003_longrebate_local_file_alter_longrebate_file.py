# Generated by Django 5.0.8 on 2024-08-18 17:51

import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_allocationautumn22_month_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='longrebate',
            name='local_file',
            field=models.FileField(blank=True, default=None, null=True, upload_to='documents/', verbose_name='Local File'),
        ),
        migrations.AlterField(
            model_name='longrebate',
            name='file',
            field=models.FileField(blank=True, default=None, null=True, storage=cloudinary_storage.storage.MediaCloudinaryStorage(), upload_to='documents/', verbose_name='File'),
        ),
    ]
