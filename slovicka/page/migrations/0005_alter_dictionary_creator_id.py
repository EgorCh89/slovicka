# Generated by Django 4.2.1 on 2023-05-18 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_alter_dictionary_creator_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictionary',
            name='creator_id',
            field=models.IntegerField(max_length=64),
        ),
    ]
