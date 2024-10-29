from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'users', UserViewSet)
router.register(r'competitions', CompetitionViewSet)
router.register(r'progress', ProgressViewSet)
router.register(r'solutions', SolutionViewSet)
router.register(r'testcases', TestCaseViewSet)
router.register(r'participants', ParticipantViewSet)
router.register(r'moderators', ModeratorViewSet)
router.register(r'admins', AdminViewSet)
router.register(r'competitionquestions', CompetitionQuestionViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace = 'rest_framework'))
]
