# Generated by Django 2.1.3 on 2018-11-25 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Office', '0004_drug_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/'),
        ),
    ]
