# Generated by Django 4.2 on 2023-11-26 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_remove_product_product_pro_id_1472ef_idx_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_model', to='product.productmodel', verbose_name='Модель'),
        ),
    ]
