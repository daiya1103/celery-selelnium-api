from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("email is must")

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=100, default="匿名")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateField()

    objects = UserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.username


from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_onetoone(sender, **kwargs):
    if kwargs["created"]:
        from scrape.models import (
            Amazon,
            Mercari,
            Yahoo,
            Rakuma,
            Paypay,
            Recipe,
            Keyword,
            Common,
        )

        Amazon.objects.create(user=kwargs["instance"])
        Mercari.objects.create(user=kwargs["instance"])
        Yahoo.objects.create(user=kwargs["instance"])
        Rakuma.objects.create(user=kwargs["instance"])
        Paypay.objects.create(user=kwargs["instance"])
        Common.objects.create(user=kwargs["instance"])
        for i in range(1, 20):
            Recipe.objects.create(user=kwargs["instance"], num=i)
