# Generated by Django 4.0.4 on 2022-05-30 12:10

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programmingLanguages', '0030_alter_language_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Текст'),
        ),
    ]
