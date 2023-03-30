from django.core.management.base import BaseCommand
from faker import Faker
from core.models import User


class Command(BaseCommand):
    help = 'Load User objects into the database'

    def handle(self, *args, **kwargs):
        faker = Faker()
        
        for i in range(1, 11):
            User.objects.create_user(
                username=faker.name(),
                email=faker.email(),
                password=f"password{i}"
            )