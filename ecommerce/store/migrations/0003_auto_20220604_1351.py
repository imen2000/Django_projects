# Generated by Django 3.2.5 on 2022-06-04 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Puzzle 3D', 'Puzzle 3D'), ('Artwall', 'Artwall'), ('Accessory', 'Accessory')], max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.category'),
        ),
    ]
