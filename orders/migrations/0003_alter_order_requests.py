# Generated by Django 3.2.13 on 2022-12-13 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_contact_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='requests',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
