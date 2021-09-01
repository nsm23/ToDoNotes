from django.core.management.base import BaseCommand
from usersapp.models import MyUsersModel


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('username', type=str)

    def handle(self, *args, **options):
        username = options['username']
        user = MyUsersModel.objects.create_superuser(username=f'{username}',
                                                     first_name=f'fname{username}',
                                                     last_name=f'lname{username}',
                                                     email=f'{username}@mail.ru',
                                                     password='geekbrains')
        print(f'Congratulation {user} create!')