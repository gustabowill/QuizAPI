from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *


class Quizz(generics.ListAPIView):

    serializer_class = QuizzSerializer
    queryset = Quizz.objects.all()


class RandomQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quizz__id=kwargs['id']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)


class QuizzQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        quizz = Question.objects.filter(quizz__id=kwargs['id'])
        serializer = QuestionSerializer(quizz, many=True)
        return Response(serializer.data)