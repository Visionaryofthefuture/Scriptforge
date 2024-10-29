from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


# Choices
difficulties = (
    ('Hard', 'hard'),
    ('Medium', 'medium'),
    ('Easy', 'easy')
)

status_choices = (
    ('Complete', 'complete'),
    ('Incomplete', 'incomplete')
)


# User model
class User(AbstractUser):
    profile_pic = models.ImageField(upload_to='media/profile_pic/')
    join_date = models.DateTimeField(auto_now=True)
    bio = models.TextField(null=True, blank=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20, unique=True)

    # Add related_name to avoid conflicts
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    def __str__(self):
        return self.username

# Question model
class Question(models.Model):
    difficulty = models.CharField(choices=difficulties, max_length=14)
    title = models.CharField(max_length=100)
    description = models.TextField(default="This is a description")
    maker = models.ForeignKey(User, on_delete=models.CASCADE, related_name="questions")
    tag = models.CharField(max_length=30)
    sample_input = models.CharField(max_length=255)
    sample_output = models.CharField(max_length=255)
    constraints = models.CharField(max_length=255)

    def __str__(self):
        return self.title


# Competition model
class Competition(models.Model):
    status = models.CharField(choices=status_choices, max_length=15)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    organiser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


# Progress model
class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    points_earned = models.IntegerField(default=0)
    status = models.CharField(choices=status_choices, max_length=15)

    def __str__(self):
        return f"{self.user.username} - {self.question.title}"


# Solution model
class Solution(models.Model):
    challenge = models.ForeignKey(Competition, on_delete=models.CASCADE)
    language = models.CharField(max_length=30)
    code = models.TextField()
    status = models.CharField(max_length=15)
    memory_used = models.IntegerField()
    test_cases_passed = models.IntegerField()

    def __str__(self):
        return f"Solution by {self.challenge}"


# TestCases model
class TestCase(models.Model):
    input_data = models.TextField()
    expected_output = models.TextField()
    is_sample_case = models.BooleanField(default=False)
    problem = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="test_cases")

    def __str__(self):
        return f"Test case for {self.problem.title}"


# Participant model
class Participant(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.person.username} in {self.competition.name}"


# Moderator model
class Moderator(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)

    def __str__(self):
        return f"Moderator: {self.person.username}"


# Admin model
class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Admin: {self.user.username}"


# CompetitionQuestion model
class CompetitionQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.question.title} in {self.competition.name}"
