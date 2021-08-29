from django.core.management.base import BaseCommand
from usersapp.models import MyUsersModel


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        MyUsersModel.objects.all().delete()
        count = options['count']
        for i in range(count):
            user = MyUsersModel.objects.create(username=f'username{i}',
                                               first_name=f'f_name{i}',
                                               last_name=f'l_name{i}',
                                               email=f'user{i}@mail{i}.ru')
            print(f'users {user} created')
        print('Done!')
