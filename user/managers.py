from django.contrib.auth.models import (
    BaseUserManager,
    )


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Użytkownik musi mieć adres email!')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        if password == None:
            password = self.make_random_password()

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user