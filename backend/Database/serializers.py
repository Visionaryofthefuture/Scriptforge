from rest_framework import serializers
from .models import *

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# Question Serializer
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

# Competition Serializer
class CompetitionSerializer(serializers.ModelSerializer):
    organiser = UserSerializer()  # Nested serializer to show organiser details

    class Meta:
        model = Competition
        fields = '__all__'

# Progress Serializer
class ProgressSerializer(serializers.ModelSerializer):
    user = UserSerializer()  
    question = QuestionSerializer()  

    class Meta:
        model = Progress
        fields = '__all__'

# Solution Serializer
class SolutionSerializer(serializers.ModelSerializer):
    challenge = CompetitionSerializer()  # Nested serializer to show challenge details

    class Meta:
        model = Solution
        fields = '__all__'

# TestCase Serializer
class TestCaseSerializer(serializers.ModelSerializer):
    problem = QuestionSerializer()  # Nested serializer to show problem details

    class Meta:
        model = TestCase
        fields = '__all__'

# Participant Serializer
class ParticipantSerializer(serializers.ModelSerializer):
    person = UserSerializer()  # Nested serializer to show person details
    competition = CompetitionSerializer()  # Nested serializer to show competition details

    class Meta:
        model = Participant
        fields = '__all__'

# Moderator Serializer
class ModeratorSerializer(serializers.ModelSerializer):
    person = UserSerializer()  # Nested serializer to show person details
    competition = CompetitionSerializer()  # Nested serializer to show competition details

    class Meta:
        model = Moderator
        fields = '__all__'

# Admin Serializer
class AdminSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Nested serializer to show user details

    class Meta:
        model = Admin
        fields = '__all__'

# CompetitionQuestion Serializer
class CompetitionQuestionSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()  # Nested serializer to show question details
    competition = CompetitionSerializer()  # Nested serializer to show competition details

    class Meta:
        model = CompetitionQuestion
        fields = '__all__'
