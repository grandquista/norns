# Generated by Django 2.0.5 on 2018-05-22 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enemy', '0005_auto_20180522_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enemy',
            name='inventory',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enemy', to='gear.Inventory'),
        ),
    ]
