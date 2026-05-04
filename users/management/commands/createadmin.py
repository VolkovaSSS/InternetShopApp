from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    help = "Создание суперпользователя"

    def handle(self, *args, **kwargs):
        user = User.objects.create(email='example@mail.ru')
        user.set_password('123456')
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        self.stdout.write(self.style.SUCCESS(f'Successfully created admin user with email {user.email}'))

