import django_filters
import json

from django.contrib.auth.models import User
from django.db import models

from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from django_filters.rest_framework import DjangoFilterBackend

from drf_yasg.utils import swagger_auto_schema

from core.serializers import *


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.serializer_class(data=request.data, context={"request": request})
        print(serializer.is_valid())
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        profile = Profile.objects.filter(user=user).first()
        if not profile:
            Profile.objects.create(user=user)
        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            {
                "token": token.key,
                "profile": ProfileSerializer(profile).data,
            }
        )


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    class Meta:
        path = "users"


class CoursePopulatedViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializerPopulated

    class Meta:
        path = "courses"


class TestPopulatedViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializerPopulated

    class Meta:
        path = "tests"


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # parser_classes = (MultiPartParser, FormParser)

    class Meta:
        path = "course"


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    class Meta:
        path = "profiles"


class ModuleViewSet(viewsets.ModelViewSet):
    serializer_class = ModuleSerializer

    def get_queryset(self):
        course_id = self.kwargs.get("course_id")  # Get the entity ID from the URL
        return Module.objects.filter(course_id=course_id)

    def create(self, request, course_id=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(entity_id=course_id)  # Associate the module with the entity
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    class Meta:
        path = "course/(?P<course_id>[^/.]+)/modules"
        basename = "course-modules"


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    class Meta:
        path = "lessons"


class UserCourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializerPopulated
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.user.id
        user_courses_ids = UsersCourse.objects.filter(user=user_id).values_list("course_id", flat=True)
        user_courses = self.queryset.filter(id__in=user_courses_ids)
        return user_courses

    class Meta:
        path = "my-courses"


class UserRegisterViewSet(viewsets.ViewSet):

    class Response(serializers.Serializer):
        token = serializers.CharField()
        user = UserSerializer()

    class Request(serializers.Serializer):
        username = serializers.CharField()
        first_name = serializers.CharField()
        last_name = serializers.CharField()
        password = serializers.CharField()

    @swagger_auto_schema(responses={200: Response}, request_body=Request)
    def create(self, request):
        data = json.loads(request.body)
        username = data.get("username")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        password = data.get("password")

        print(password)

        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        profile = Profile.objects.create(user=user)
        token, _ = Token.objects.get_or_create(user=user)

        return Response(
            {
                "token": token.key,
                "profile": ProfileSerializer(profile).data,
            }
        )

    class Meta:
        path = "register"
