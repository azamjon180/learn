# Generated by Django 3.0.3 on 2020-09-17 03:54

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_auto_20200916_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='service')),
                ('icon', models.TextField(blank=True, null=True)),
                ('link', models.CharField(blank=True, max_length=64, null=True)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]