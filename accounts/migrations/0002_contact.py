# Generated by Django 3.2.4 on 2021-07-24 03:01

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('subject', models.CharField(max_length=30)),
                ('message', models.TextField()),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Xabar',
                'verbose_name_plural': 'Xabarlar',
            },
        ),
    ]
