# Generated by Django 2.2.7 on 2019-11-12 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20191112_0824'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=40)),
                ('deskripsi', models.TextField()),
                ('waktu_tayang', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200)),
                ('nomor_telepon', models.IntegerField(default=0)),
                ('email', models.EmailField(default='no-email@gmail.com', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film_id', models.SmallIntegerField(default=0)),
                ('kursi_id', models.CharField(max_length=3)),
                ('tipe', models.CharField(max_length=10)),
                ('harga', models.SmallIntegerField(default=0)),
                ('ketersediaan', models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='email',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='harga',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='nama',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='nomor_telepon',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='nomor_tiket',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='pesan',
        ),
        migrations.AddField(
            model_name='ticket',
            name='film_id',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ticket',
            name='kursi_id',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ticket',
            name='order_id',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ticket',
            name='tiket_code',
            field=models.SmallIntegerField(default=0),
        ),
    ]
