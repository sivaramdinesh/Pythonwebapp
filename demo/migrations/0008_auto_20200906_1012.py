# Generated by Django 3.1.1 on 2020-09-06 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0007_auto_20200906_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='Cover',
            field=models.ImageField(blank=True, upload_to='covers/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='Published_date',
            field=models.DateField(),
        ),
    ]
