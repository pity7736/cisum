from .factories import GenreFactory


def test_str():
    genre = GenreFactory.build()
    assert genre.__str__() == 'punk'
