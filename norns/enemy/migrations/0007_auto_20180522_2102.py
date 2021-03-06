# Generated by Django 2.0.5 on 2018-05-22 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0006_room_grid_size'),
        ('enemy', '0006_auto_20180522_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnemyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unnamed', max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='enemy',
            name='tiles',
        ),
        migrations.AddField(
            model_name='enemy',
            name='tile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.Tile'),
        ),
        migrations.AlterField(
            model_name='enemy',
            name='inventory',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gear.Inventory'),
        ),
        migrations.AlterField(
            model_name='enemy',
            name='weapon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gear.Weapon'),
        ),
        migrations.AddField(
            model_name='enemy',
            name='enemy_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='enemy.EnemyType'),
        ),
    ]
