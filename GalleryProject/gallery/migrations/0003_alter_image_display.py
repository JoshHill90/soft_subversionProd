# Generated by Django 4.2.3 on 2023-11-23 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_dispaly_remove_image_display_image_display'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='display',
            field=models.ManyToManyField(blank=True, null=True, to='gallery.dispaly'),
        ),
    ]