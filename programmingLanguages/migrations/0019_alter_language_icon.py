# Generated by Django 4.0.4 on 2022-04-25 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programmingLanguages', '0018_alter_language_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='icon',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
