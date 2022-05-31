# Generated by Django 4.0.4 on 2022-05-31 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programmingLanguages', '0033_alter_language_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='URL'),
        ),
    ]