import factory

from accounts.models import User


class UserFactory(factory.django.DjangoModelFactory):
    email = 'pity7736@gmail.com'
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')

    class Meta:
        django_get_or_create = ('email',)
        model = User
