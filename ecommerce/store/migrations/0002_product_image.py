# Generated by Django 3.2.5 on 2021-08-21 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default.jpeg', upload_to='product_pics'),
        ),
    ]