from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

from core.enums import UserRole, Status, QuestionType


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.IntegerField(choices=UserRole.choices(), default=UserRole.USER.value, verbose_name="role")
    phone = models.CharField(max_length=256, default="", blank=True)
    avatar_url = models.TextField(blank=True, default="", verbose_name="avatar_url")

    def get_full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def __str__(self):
        return f"#{self.id}: {self.get_full_name()}"


class Course(models.Model):
    title = models.TextField(blank=True, default="", verbose_name="title")
    description = models.TextField(blank=True, default="", verbose_name="description")
    img_url = models.TextField(blank=True, default="", verbose_name="img_url")

    def __str__(self):
        return f"#{self.id}: {self.title}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    # status = models.IntegerField(choices=Status.choices(), default=Status.NOT_STARTED.value, verbose_name="status")


class UsersCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="users_courses",
        related_query_name="users_course",
    )
    status = models.IntegerField(choices=Status.choices(), default=Status.NOT_STARTED.value, verbose_name="status")

    def __str__(self):
        return f"#{self.user}: {self.course}, {self.status}"


class Module(models.Model):
    title = models.TextField(blank=True, default="", verbose_name="title")
    description = models.TextField(blank=True, default="", verbose_name="description")
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, null=False, blank=False, related_name="modules", related_query_name="module"
    )

    def __str__(self):
        return f"#{self.id}: {self.title}"

    class Meta:
        verbose_name = "Модуль"
        verbose_name_plural = "Модули"


class Lesson(models.Model):
    title = models.TextField(blank=True, default="", verbose_name="title")
    description = models.TextField(blank=True, default="", verbose_name="description")
    module = models.ForeignKey(
        Module, on_delete=models.CASCADE, null=False, blank=False, related_name="lessons", related_query_name="lesson"
    )
    content = models.TextField(blank=True, default="", verbose_name="content")

    def __str__(self):
        return f"#{self.id}: {self.title}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class UsersLesson(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="users_lessons",
        related_query_name="users_lesson",
    )
    status = models.IntegerField(choices=Status.choices(), default=Status.NOT_STARTED.value, verbose_name="status")

    def __str__(self):
        return f"#{self.user}: {self.lesson}, {self.status}"


class Test(models.Model):
    title = models.TextField(blank=True, default="", verbose_name="title")
    description = models.TextField(blank=True, default="", verbose_name="description")
    module = models.OneToOneField(
        Module,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="test",
        related_query_name="test",
    )

    def __str__(self):
        return f"#{self.id}: {self.title} {self.module}"


class Question(models.Model):
    text = models.TextField(blank=True, default="", verbose_name="text")
    type = models.IntegerField(choices=QuestionType.choices(), verbose_name="type")
    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="questions",
        related_query_name="question",
    )

    def __str__(self):
        return f"#{self.id}: {self.text}"


class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="answers",
        related_query_name="answer",
    )
    text = models.TextField(blank=True, default="", verbose_name="text")
    is_correct = models.BooleanField(default=False, verbose_name="is_correct")

    def __str__(self):
        return f"#{self.id}: {self.question} {self.text}"


class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=False, blank=False)
    text = models.TextField(blank=True, default="", verbose_name="text")

    def __str__(self):
        return f"#{self.id}: {self.question} {self.text}"
