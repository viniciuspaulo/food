# Generated by Django 2.1.5 on 2020-01-02 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_auto_20191231_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='lat',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='lng',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]