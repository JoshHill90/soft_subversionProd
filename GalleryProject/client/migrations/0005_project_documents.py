# Generated by Django 4.2.3 on 2023-11-12 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0002_document'),
        ('client', '0004_rename_cleint_id_projectrequest_client_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='documents',
            field=models.ManyToManyField(to='site_app.document'),
        ),
    ]
