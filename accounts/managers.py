from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra):
        extra['is_staff'] = False
        extra['is_superuser'] = False
        return self._create_user(email=email, password=password, **extra)

    def create_superuser(self, email, password, **extra):
        assert password, 'password is obligatory!'
        extra['is_staff'] = True
        extra['is_superuser'] = True
        return self._create_user(email=email, password=password, **extra)

    def _create_user(self, email, password, **extra):
        email = self.normalize_email(email=email)
        user = self.model(email=email, **extra)
        user.set_password(password)
        user.save()
        return user
