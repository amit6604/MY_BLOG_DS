# Generated by Django 3.0.1 on 2020-01-04 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200104_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogging',
            name='blog_series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.BloggingSeries', verbose_name='Series'),
        ),
    ]