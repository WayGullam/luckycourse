# Generated by Django 4.2.8 on 2024-08-04 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_test_module'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='is_correct',
            field=models.BooleanField(default=False, verbose_name='is_correct'),
        ),
        migrations.AlterField(
            model_name='test',
            name='module',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='test', related_query_name='test', to='core.module'),
        ),
    ]
