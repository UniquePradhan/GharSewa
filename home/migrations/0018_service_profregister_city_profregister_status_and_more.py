# Generated by Django 4.2.2 on 2023-07-13 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('service_id', models.AutoField(primary_key=True, serialize=False)),
                ('service_name', models.CharField(max_length=50)),
                ('service_desc', models.TextField()),
                ('image', models.FileField(null=True, upload_to='')),
                ('pub_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='profregister',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.city'),
        ),
        migrations.AddField(
            model_name='profregister',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.status'),
        ),
        migrations.AddField(
            model_name='profregister',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.service'),
        ),
    ]
