# Generated by Django 4.2.5 on 2023-09-22 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_open', models.BooleanField(default=True)),
                ('location', models.CharField(max_length=255)),
                ('metro', models.CharField(max_length=255)),
                ('open_time', models.DateTimeField()),
                ('close_time', models.DateTimeField()),
            ],
        ),
    ]
