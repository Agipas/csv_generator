# Generated by Django 4.1.7 on 2023-02-28 15:18

from django.db import migrations, models
import generating_csv.models


class Migration(migrations.Migration):

    dependencies = [
        ('generating_csv', '0002_alter_datascheme_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datascheme',
            name='file',
            field=models.FileField(),
        ),
    ]
