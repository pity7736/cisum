from pytest import mark, raises

from accounts.models import User


@mark.django_db
def test_regular_user_with_password():
    user = User.objects.create_user(email='pity7736@gmail.com', password='julian.cortes')
    assert user.is_staff is False
    assert user.is_superuser is False
    assert user.has_usable_password() is True


@mark.django_db
def test_regular_user_with_extra_fields():
    user = User.objects.create_user(
        email='pity7736@gmail.com',
        password='julian.cortes',
        first_name='julian',
        last_name='cortes',
    )
    assert user.first_name == 'julian'
    assert user.last_name == 'cortes'


@mark.django_db
def test_regular_user_without_password():
    user = User.objects.create_user(email='pity7736@gmail.com')
    assert user.is_staff is False
    assert user.is_superuser is False
    assert user.has_usable_password() is False


@mark.django_db
def test_superuser_with_password():
    user = User.objects.create_superuser(email='pity7736@gmail.com', password='julian.cortes')
    assert user.is_staff is True
    assert user.is_superuser is True
    assert user.has_usable_password() is True


def test_superuser_with_password_none():
    with raises(AssertionError):
        User.objects.create_superuser(email='pity7736@gmail.com', password=None)


@mark.django_db
def test_superuser_with_extra_fields():
    user = User.objects.create_superuser(
        email='pity7736@gmail.com',
        password='julian.cortes',
        first_name='julian',
        last_name='cortes',
    )
    assert user.first_name == 'julian'
    assert user.last_name == 'cortes'
