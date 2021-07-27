# Generated by Django 3.2.4 on 2021-07-24 03:04

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminContactPhones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
            options={
                'verbose_name': 'Contact Phone',
                'verbose_name_plural': 'Contact Phones',
                'managed': True,
            },
        ),
    ]