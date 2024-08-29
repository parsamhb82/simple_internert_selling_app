# Generated by Django 5.1 on 2024-08-29 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('internet_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('is_active', models.BooleanField(default=False)),
                ('internet', models.ManyToManyField(blank=True, to='internet_app.internet')),
            ],
        ),
    ]
