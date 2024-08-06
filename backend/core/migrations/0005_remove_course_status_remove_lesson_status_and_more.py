# Generated by Django 4.2.8 on 2024-08-03 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_course_img_url_alter_lesson_module_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='status',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='status',
        ),
        migrations.RemoveField(
            model_name='module',
            name='status',
        ),
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.IntegerField(choices=[(1, 'MULTIPLE'), (2, 'SINGLE'), (3, 'INPUT')], verbose_name='type'),
        ),
    ]