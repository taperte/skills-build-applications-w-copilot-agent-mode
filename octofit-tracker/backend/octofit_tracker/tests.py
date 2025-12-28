from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='TestTeam', description='desc')
        self.assertEqual(str(team), 'TestTeam')
    def test_user_create(self):
        team = Team.objects.create(name='T', description='d')
        user = User.objects.create(email='a@b.com', username='A', team=team, is_superhero=True)
        self.assertEqual(str(user), 'A')
    def test_activity_create(self):
        team = Team.objects.create(name='T2', description='d2')
        user = User.objects.create(email='b@b.com', username='B', team=team, is_superhero=True)
        activity = Activity.objects.create(user=user, activity_type='Run', duration=10, date='2025-01-01')
        self.assertEqual(str(activity), 'B - Run')
    def test_workout_create(self):
        workout = Workout.objects.create(name='W', description='desc')
        self.assertEqual(str(workout), 'W')
    def test_leaderboard_create(self):
        team = Team.objects.create(name='T3', description='d3')
        user = User.objects.create(email='c@b.com', username='C', team=team, is_superhero=True)
        lb = Leaderboard.objects.create(user=user, score=42)
        self.assertEqual(str(lb), 'C - 42')
