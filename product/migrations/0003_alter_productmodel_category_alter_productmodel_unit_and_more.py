# Generated by Django 4.0.4 on 2022-05-08 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_unitmodel_conversion_ratio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.categorymodel'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.unitmodel'),
        ),
        migrations.AlterField(
            model_name='unitmodel',
            name='base_unit',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='unitmodel',
            name='secondary_unit',
            field=models.CharField(max_length=20),
        ),
    ]
