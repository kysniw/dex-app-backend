from django.contrib.auth.models import (
    BaseUserManager,
    )
from django.core.mail import send_mail
from dexapp.settings import EMAIL_HOST_USER

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Użytkownik musi mieć adres email!')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        if password == None:
            password = self.make_random_password()
            send_mail(
            'Witaj w systemie DEX',
            f'Oto Twoje hasło startowe: {password}',
            EMAIL_HOST_USER,
            [f'{email}']
        )

        user.set_password(password)
        user.is_staff = False
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user