# Generated by Django 2.1.3 on 2018-11-25 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Office', '0003_drug_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
