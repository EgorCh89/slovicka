# Generated by Django 4.2.1 on 2023-05-18 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_alter_dictionary_creator_id_alter_dictionary_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictionary',
            name='creator_id',
            field=models.IntegerField(),
        ),
    ]
