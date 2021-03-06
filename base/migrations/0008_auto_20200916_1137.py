# Generated by Django 3.0.3 on 2020-09-16 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_amazon'),
    ]

    operations = [
        migrations.AddField(
            model_name='amazon',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='amazon',
            name='link',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='amazon',
            name='number_1',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='amazon',
            name='number_2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='amazon',
            name='number_3',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]
