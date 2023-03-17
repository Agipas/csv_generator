# Generated by Django 4.1.7 on 2023-03-03 21:56

from django.db import migrations, models
import generating_csv.models


class Migration(migrations.Migration):

    dependencies = [
        ('generating_csv', '0008_dataset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='file',
            field=models.FileField(blank=True, upload_to=generating_csv.models.DataSet.upload_file_to),
        ),
    ]