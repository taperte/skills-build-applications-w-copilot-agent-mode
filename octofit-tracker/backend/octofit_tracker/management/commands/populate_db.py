
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Drop collections using PyMongo
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        db.activity.drop()
        db.leaderboard.drop()
        db.workout.drop()
        db.user.drop()
        db.team.drop()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create users
        users = []
        users.append(User.objects.create(email='tony@stark.com', username='IronMan', team=marvel, is_superhero=True))
        users.append(User.objects.create(email='steve@rogers.com', username='CaptainAmerica', team=marvel, is_superhero=True))
        users.append(User.objects.create(email='bruce@wayne.com', username='Batman', team=dc, is_superhero=True))
        users.append(User.objects.create(email='clark@kent.com', username='Superman', team=dc, is_superhero=True))

        # Create activities
        for user in users:
            Activity.objects.create(user=user, activity_type='Running', duration=30, date=timezone.now().date())
            Activity.objects.create(user=user, activity_type='Cycling', duration=45, date=timezone.now().date())

        # Create workouts
        workout1 = Workout.objects.create(name='Super Strength', description='Strength training for superheroes')
        workout2 = Workout.objects.create(name='Flight Training', description='Aerobic workout for flying heroes')
        workout1.suggested_for.set(users)
        workout2.suggested_for.set(users)

        # Create leaderboard
        for user in users:
            Leaderboard.objects.create(user=user, score=100)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
