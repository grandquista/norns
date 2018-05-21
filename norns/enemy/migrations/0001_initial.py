# Generated by Django 2.0.5 on 2018-05-21 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('status', '0001_initial'),
        ('room', '0001_initial'),
        ('gear', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enemy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('abilities', models.ManyToManyField(blank=True, to='status.Ability')),
                ('loot', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='gear.Weapon')),
                ('tiles', models.ManyToManyField(blank=True, related_name='enemies', to='room.Tile')),
            ],
        ),
    ]