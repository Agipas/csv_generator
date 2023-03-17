# Generated by Django 4.1.7 on 2023-02-28 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import generating_csv.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DataScheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(db_index=True, max_length=200)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=100)),
                ('file', models.FileField()),
                ('column_separator', models.CharField(choices=[(',', 'Comma (,)'), ('.', 'Semicolon (;)'), ('|', 'Pipe (|)')], max_length=50)),
                ('string_character', models.CharField(choices=[('"', 'Double quotes("..")'), ("'", "Single quotes ('..')")], max_length=50)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Data Scheme',
                'verbose_name_plural': 'Data Schemes',
                'ordering': ['-date_updated'],
            },
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('type', models.CharField(choices=[('full_name', 'Full name'), ('job', 'Job'), ('email', 'Email'), ('domain_name', 'Domain name'), ('phon_number', 'Phone number'), ('company_name', 'Company name'), ('text', 'Text'), ('integer', 'Integer'), ('address', 'Address'), ('date', 'Date')], max_length=100)),
                ('order', models.IntegerField(default=0)),
                ('range_from', models.IntegerField(null=True)),
                ('range_to', models.IntegerField(null=True)),
                ('data_scheme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='generating_csv.datascheme')),
            ],
            options={
                'verbose_name': 'Column',
                'verbose_name_plural': 'Columns',
                'ordering': ['name'],
            },
        ),
    ]
