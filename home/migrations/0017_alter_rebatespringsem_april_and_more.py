# Generated by Django 4.1.7 on 2023-04-27 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_rebateautumnsem_august_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rebatespringsem',
            name='april',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='rebatespringsem',
            name='feburary',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='rebatespringsem',
            name='january',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='rebatespringsem',
            name='june',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='rebatespringsem',
            name='march',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='rebatespringsem',
            name='may',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
