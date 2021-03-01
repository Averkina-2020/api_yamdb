from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **kwargs):
        if not email:
            raise ValueError('Почта должна быть указана')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, username, **kwargs):
        user = self.model(
            email=email,
            password=password,
            username=username,
            role='admin',
            **kwargs,
        )
        user.is_admin = True
        user.save(using=self._db)

        return user
