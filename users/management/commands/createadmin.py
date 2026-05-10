from django.core.management.base import BaseCommand
from users.models import CustomUser
from config.settings import ADMIN_EMAIL
from config.settings import ADMIN_PASSWORD


class Command(BaseCommand):
    help = "Создание суперпользователя"

    def handle(self, *args, **kwargs):
        user = CustomUser.objects.create(email=ADMIN_EMAIL)
        user.set_password(ADMIN_PASSWORD)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully created admin user with email {user.email}"
            )
        )
