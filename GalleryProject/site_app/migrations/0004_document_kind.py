# Generated by Django 4.2.3 on 2023-11-14 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0003_document_created_document_doc_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='kind',
            field=models.CharField(blank=True, choices=[('pdf', 'pdf'), ('docx', 'docx')], max_length=50, null=True),
        ),
    ]