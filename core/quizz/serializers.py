from rest_framework import serializers
from .models import *

class QuizzSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quizz
        fields = "__all__"


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['id', 'answer_text', 'is_right']


class RandomQuestionSerializer(serializers.ModelSerializer):

    answer = serializers.StringRelatedField(many=True)

    class Meta:
        model = Question
        fields = ['id', 'title', 'answer']


class QuestionSerializer(serializers.ModelSerializer):
    answer_set = AnswerSerializer(many=True, read_only=True)
    quizz = QuizzSerializer(read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'title', 'answer_set', 'quizz']

