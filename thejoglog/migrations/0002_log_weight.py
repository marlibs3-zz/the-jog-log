# Generated by Django 2.2.7 on 2019-11-12 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thejoglog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='weight',
            field=models.FloatField(default=5),
            preserve_default=False,
        ),
    ]