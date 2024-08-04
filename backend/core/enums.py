from enum import Enum
from http.client import PROCESSING


class UserRole(Enum):
    ADMIN = 1
    TEACHER = 2
    USER = 3

    @classmethod
    def choices(cls):
        return [(tag.value, tag.name) for tag in cls]


class Status(Enum):
    NOT_STARTED = 1
    IN_PROGRESS = 2
    COMPLETED = 3

    @classmethod
    def choices(cls):
        return [(tag.value, tag.name) for tag in cls]


class QuestionType(Enum):
    MULTIPLE = 1
    SINGLE = 2
    INPUT = 3

    @classmethod
    def choices(cls):
        return [(tag.value, tag.name) for tag in cls]
