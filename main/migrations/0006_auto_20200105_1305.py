# Generated by Django 3.0.1 on 2020-01-05 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200104_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogging',
            name='blog_series',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.BloggingSeries', verbose_name='Series'),
        ),
    ]
