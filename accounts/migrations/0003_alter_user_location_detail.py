# Generated by Django 3.2.13 on 2022-12-06 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_location_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='location_detail',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]