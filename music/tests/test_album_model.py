from .factories import AlbumFactory


def test_str():
    album = AlbumFactory.build()
    assert album.__str__() == 'los olvidados - los muertos de cristo'
