from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet

router = DefaultRouter()
router.register(r'questions', QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace = 'rest_framework'))
]
