# Generated by Django 2.2.7 on 2019-12-01 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artistas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cancion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('artista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artistas.Artista')),
            ],
        ),
    ]
