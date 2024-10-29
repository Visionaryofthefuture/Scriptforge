# views.py
from rest_framework import viewsets
from .models import Question
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import QuestionSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
