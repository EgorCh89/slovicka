# Generated by Django 4.2.1 on 2023-05-18 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_dictionary_creator_id_dictionary_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictionary',
            name='creator_id',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='dictionary',
            name='name',
            field=models.TextField(default=None, unique=True),
        ),
    ]
