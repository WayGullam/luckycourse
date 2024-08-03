# Generated by Django 4.2.8 on 2023-12-29 07:46

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_meal_restaurant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, default='', max_length=256)),
                ('reward_points', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delivery', models.BooleanField(default=True, verbose_name='is_delivery')),
                ('is_present', models.BooleanField(default=True, verbose_name='is_delivery')),
                ('address', models.TextField(blank=True, default='', verbose_name='address')),
                ('note', models.TextField(blank=True, default='', verbose_name='address')),
                ('payment_method', models.CharField(choices=[('ONLINE', 'ONLINE'), ('COURIER', 'COURIER'), ('CASH', 'CASH')], default='ONLINE', max_length=128, verbose_name='payment_method')),
                ('payment_status', models.CharField(choices=[('PAYED', 'PAYED'), ('PENDING', 'PENDING'), ('FAILED', 'FAILED')], default='PENDING', max_length=128, verbose_name='payment_method')),
                ('delivery_time', models.DateTimeField(null=True, verbose_name='created_at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.client')),
                ('to_whom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='present_senders', related_query_name='present_sender', to='core.client')),
            ],
            options={
                'verbose_name': 'Ресторан',
                'verbose_name_plural': 'Рестораны',
            },
        ),
        migrations.AlterModelOptions(
            name='restaurant',
            options={'ordering': ['-id'], 'verbose_name': 'Ресторан', 'verbose_name_plural': 'Рестораны'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.TextField(blank=True, default='', verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.TextField(blank=True, default='', verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='image',
            field=models.TextField(blank=True, default='', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='name',
            field=models.TextField(blank=True, default='', verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='address',
            field=models.TextField(blank=True, default='', verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=models.TextField(blank=True, default='', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.TextField(blank=True, default='', verbose_name='name'),
        ),
        migrations.CreateModel(
            name='OrderMeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='quantity')),
                ('notes', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1024), blank=True, default=[], size=None)),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_meals', related_query_name='order_meal', to='core.meal')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meals', related_query_name='meal', to='core.order')),
            ],
            options={
                'verbose_name': 'Ресторан',
                'verbose_name_plural': 'Рестораны',
            },
        ),
        migrations.AddField(
            model_name='client',
            name='restaurant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.restaurant'),
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
