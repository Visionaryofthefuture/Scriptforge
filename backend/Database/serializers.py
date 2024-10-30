from rest_framework import serializers
from .models import *
from dj_rest_auth.registration.serializers import RegisterSerializer

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

#User Register
class CustomRegisterSerializer(RegisterSerializer):
    profile_picture = serializers.ImageField(required=False)
    bio = serializers.CharField(max_length=255, required=False)
    join_date = serializers.DateField(read_only=True)

    def custom_signup(self, request, user):
        user.profile_picture = self.validated_data.get('profile_picture', '')
        user.bio = self.validated_data.get('bio', '')
        user.save(update_fields=['profile_picture', 'bio'])