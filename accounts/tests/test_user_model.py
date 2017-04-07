from pytest import mark

from accounts.tests.factories import UserFactory


def test_str_user():
    user = UserFactory.build(first_name='julian', last_name='cortes')
    assert user.__str__() == 'julian cortes'

names = (
    (None, None),
    ('julian', None),
    (None, 'cortes')
)


@mark.parametrize('first_name,last_name', names)
def test_str_user_without_first_name_or_last_name(first_name, last_name):
    user = UserFactory.build(email='pity7736@gmail.com', first_name=first_name, last_name=last_name)
    assert user.__str__() == 'pity7736@gmail.com'


def test_get_full_name():
    user = UserFactory.build(first_name='julian', last_name='cortes')
    assert user.get_full_name() == 'julian cortes'


@mark.parametrize('first_name,last_name', names)
def test_et_full_name_without_first_name_or_last_name(first_name, last_name):
    user = UserFactory.build(email='pity7736@gmail.com', first_name=first_name, last_name=last_name)
    assert user.get_full_name() == 'pity7736@gmail.com'
