# Generated by Django 2.0.4 on 2018-04-18 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stu', '0008_company_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='email',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
