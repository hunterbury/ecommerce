# Generated by Django 3.2.8 on 2021-12-07 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20211205_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='images',
            field=models.URLField(),
        ),
    ]