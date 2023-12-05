# Generated by Django 4.1.13 on 2023-12-05 11:46

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tabo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scraped',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('time', models.CharField(max_length=128)),
                ('temperature', models.FloatField()),
            ],
            options={
                'verbose_name': 'Tabo Minutes Data',
                'verbose_name_plural': 'Tabo Minutes Data',
                'db_table': 'scraped_data',
            },
        ),
    ]