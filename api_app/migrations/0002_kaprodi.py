# Generated by Django 4.2.1 on 2023-05-23 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kaprodi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nip', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=255)),
                ('nama', models.CharField(max_length=100)),
            ],
        ),
    ]