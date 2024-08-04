# Generated by Django 4.2.8 on 2024-08-04 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_course_img_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='module',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='tests', related_query_name='test', to='core.module'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', related_query_name='answer', to='core.question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', related_query_name='question', to='core.test'),
        ),
    ]
