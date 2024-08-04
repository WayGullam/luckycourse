from django.contrib.auth.models import Group, User
from rest_framework import serializers

from core.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name"]


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        exclude = ["module"]


class ModuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Module
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        exclude = ["question"]


class QuestionSerializerPopulated(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        exclude = ["test"]


class TestSerializerPopulated(serializers.ModelSerializer):
    questions = QuestionSerializerPopulated(many=True)

    def create(self, validated_data):
        questions_data = validated_data.pop("questions")  # Extract questions data
        test = Test.objects.create(**validated_data)  # Create the course
        for question_data in questions_data:
            answers_data = question_data.pop("answers")
            question = Question.objects.create(test=test, **question_data)  # Create each module

            for answer_data in answers_data:
                Answer.objects.create(question=question, **answer_data)

        return test

    class Meta:
        model = Test
        exclude = ["module"]


class ModuleSerializerPopulated(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True)
    test = TestSerializerPopulated()

    class Meta:
        model = Module
        exclude = ["course"]


class CourseSerializerPopulated(serializers.ModelSerializer):
    modules = ModuleSerializerPopulated(many=True)

    def create(self, validated_data):
        modules_data = validated_data.pop("modules")  # Extract modules data
        course = Course.objects.create(**validated_data)  # Create the course
        for module_data in modules_data:
            lessons_data = module_data.pop("lessons")
            test_data = module_data.pop("test")
            module = Module.objects.create(course=course, **module_data)  # Create each module
            if test_data:
                test_data["module"] = module
                test_serializer = TestSerializerPopulated()
                test_serializer.create(test_data)

            for lesson_data in lessons_data:
                Lesson.objects.create(module=module, **lesson_data)

        return course

    class Meta:
        model = Course
        fields = "__all__"
