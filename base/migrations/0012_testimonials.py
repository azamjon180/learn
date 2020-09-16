# Generated by Django 3.0.3 on 2020-09-16 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='testimonials')),
                ('link', models.CharField(blank=True, max_length=64, null=True)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]