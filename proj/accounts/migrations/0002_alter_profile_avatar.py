# Generated by Django 3.2.6 on 2021-08-07 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(height_field=250, upload_to='images/', width_field=380),
        ),
    ]