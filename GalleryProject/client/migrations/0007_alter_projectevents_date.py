# Generated by Django 4.2.3 on 2023-11-15 06:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_remove_projectterms_project_docs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectevents',
            name='date',
            field=models.DateField(default=datetime.date(2023, 11, 15)),
        ),
    ]
