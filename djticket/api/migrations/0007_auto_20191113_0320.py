# Generated by Django 2.2.7 on 2019-11-13 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20191112_1105'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('created_at',), 'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterModelOptions(
            name='seat',
            options={'ordering': ('seat_num',), 'verbose_name_plural': 'Seats'},
        ),
        migrations.RemoveField(
            model_name='order',
            name='seat_id',
        ),
        migrations.RemoveField(
            model_name='seat',
            name='movie_id',
        ),
        migrations.AddField(
            model_name='order',
            name='seat',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='api.Seat'),
        ),
        migrations.AddField(
            model_name='seat',
            name='movie',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='api.Movie'),
        ),
    ]
