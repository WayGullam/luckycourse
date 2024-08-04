# Generated by Django 4.2.8 on 2024-08-04 00:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0005_remove_course_status_remove_lesson_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='text',
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='UsersLesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'NOT_STARTED'), (2, 'IN_PROGRESS'), (3, 'COMPLETED')], default=1, verbose_name='status')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_lessons', related_query_name='users_lesson', to='core.lesson')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UsersCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'NOT_STARTED'), (2, 'IN_PROGRESS'), (3, 'COMPLETED')], default=1, verbose_name='status')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_courses', related_query_name='users_course', to='core.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
