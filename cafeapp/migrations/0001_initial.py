# Generated by Django 3.2.8 on 2021-10-06 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.BigAutoField(help_text='Cafe ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, null=True)),
                ('content', models.TextField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='profile/')),
                ('name', models.CharField(max_length=20, null=True)),
                ('content', models.TextField(max_length=500, null=True)),
                ('price', models.IntegerField()),
                ('isSoldOut', models.BooleanField()),
                ('cafe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cafe_product', to='cafeapp.cafe')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(help_text='Order ID', primary_key=True, serialize=False)),
                ('cafe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cafe_order', to='cafeapp.cafe')),
            ],
        ),
    ]
