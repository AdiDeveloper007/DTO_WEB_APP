# Generated by Django 3.2.5 on 2021-07-19 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dto', '0013_auto_20210719_2031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='four',
            name='address',
        ),
        migrations.RemoveField(
            model_name='nongear',
            name='address',
        ),
        migrations.RemoveField(
            model_name='two',
            name='address',
        ),
        migrations.AlterField(
            model_name='four',
            name='chalantype',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='nongear',
            name='chalantype',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='two',
            name='chalantype',
            field=models.CharField(max_length=50, null=True),
        ),
    ]