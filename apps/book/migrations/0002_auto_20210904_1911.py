# Generated by Django 3.2.6 on 2021-09-05 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['name'], 'verbose_name': 'Author', 'verbose_name_plural': 'Authors'},
        ),
        migrations.AlterField(
            model_name='author',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
