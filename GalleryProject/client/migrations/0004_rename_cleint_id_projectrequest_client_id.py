# Generated by Django 4.2.3 on 2023-11-08 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_remove_projectrequest_user_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectrequest',
            old_name='cleint_id',
            new_name='client_id',
        ),
    ]
