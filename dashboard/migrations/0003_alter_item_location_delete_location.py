# Generated by Django 4.2.14 on 2024-08-02 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_rename_best_before_item_expiry_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='location',
            field=models.IntegerField(choices=[(0, 'Fridge'), (1, 'Freezer')], default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]