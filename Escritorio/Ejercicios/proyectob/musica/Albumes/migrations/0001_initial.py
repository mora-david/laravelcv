# Generated by Django 2.2.7 on 2019-12-03 21:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albumes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha', models.DateField(default=datetime.datetime(2019, 12, 3, 21, 28, 2, 937588, tzinfo=utc))),
            ],
        ),
    ]
