# Generated by Django 3.2.5 on 2021-07-15 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dto', '0006_auto_20210715_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signin',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
