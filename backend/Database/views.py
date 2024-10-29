from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import (
    User, Question, Competition, Progress, Solution, TestCase, Participant,
    Moderator, Admin, CompetitionQuestion
)
from .serializers import (
    UserSerializer, QuestionSerializer, CompetitionSerializer, ProgressSerializer,
    SolutionSerializer, TestCaseSerializer, ParticipantSerializer, ModeratorSerializer,
    AdminSerializer, CompetitionQuestionSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'tag']
    ordering_fields = ['difficulty', 'title']

    @action(detail=False, methods=['get'], url_path='difficulty/(?P<level>[^/.]+)')
    def filter_by_difficulty(self, request, level=None):
        filtered_questions = Question.objects.filter(difficulty=level)
        serializer = self.get_serializer(filtered_questions, many=True)
        return Response(serializer.data)


class CompetitionViewSet(viewsets.ModelViewSet):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['start_date', 'end_date']


class ProgressViewSet(viewsets.ModelViewSet):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class SolutionViewSet(viewsets.ModelViewSet):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['language', 'status']


class TestCaseViewSet(viewsets.ModelViewSet):
    queryset = TestCase.objects.all()
    serializer_class = TestCaseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ModeratorViewSet(viewsets.ModelViewSet):
    queryset = Moderator.objects.all()
    serializer_class = ModeratorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CompetitionQuestionViewSet(viewsets.ModelViewSet):
    queryset = CompetitionQuestion.objects.all()
    serializer_class = CompetitionQuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
