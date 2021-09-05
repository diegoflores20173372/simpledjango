# Generated by Django 3.2.6 on 2021-09-04 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
    ]