# Generated by Django 4.2.10 on 2024-03-12 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0002_remove_coupon_discount_coupon_discount_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='discount_name',
            new_name='coupon_name',
        ),
    ]
