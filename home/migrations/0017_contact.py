# Generated by Django 4.2.2 on 2023-07-10 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_city_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('content', models.TextField()),
                ('timeStamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
