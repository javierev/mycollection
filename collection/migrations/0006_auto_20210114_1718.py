# Generated by Django 3.1.4 on 2021-01-14 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0005_auto_20210105_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='collection.country'),
        ),
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.SmallAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='console',
            name='id',
            field=models.SmallAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='country',
            name='id',
            field=models.SmallAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='game',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]