# Generated by Django 4.1.7 on 2023-03-03 11:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('generating_csv', '0005_alter_datascheme_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='data_scheme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='column_scheme', to='generating_csv.datascheme'),
        ),
        migrations.AlterField(
            model_name='datascheme',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
