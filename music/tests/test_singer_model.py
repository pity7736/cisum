from pytest import mark

from .factories import SingerFactory


@mark.django_db
def test_name_slug():
    singer = SingerFactory.create()
    assert singer.name_slug == 'los-muertos-de-cristo'


def test_str():
    singer = SingerFactory.build()
    assert singer.__str__() == 'los muertos de cristo'
