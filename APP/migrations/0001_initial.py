# Generated by Django 4.2.10 on 2024-02-20 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_cookie_id', models.AutoField(primary_key=True, serialize=False)),
                ('total_amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('coupon_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.FloatField()),
                ('discount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('expiry_date', models.DateField()),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('contact', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('total_amount', models.FloatField()),
                ('delivery_by_date', models.DateField()),
                ('status', models.CharField(max_length=255)),
                ('payment_details', models.TextField()),
                ('transaction_id', models.CharField(max_length=255)),
                ('coupon_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='APP.coupon')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.user')),
            ],
        ),
    ]
