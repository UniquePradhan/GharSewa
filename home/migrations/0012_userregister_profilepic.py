# Generated by Django 4.2.2 on 2023-07-04 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_userregister_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregister',
            name='profilePic',
            field=models.ImageField(null=True, upload_to='customers_pic/'),
        ),
    ]