# Generated by Django 5.0 on 2024-08-30 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_support_more2_support_more3_support_title2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image',
            new_name='name',
        ),
    ]
