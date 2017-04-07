from .factories import SongFactory


def test_str():
    song = SongFactory.build(name='ni dios ni amo')
    assert song.__str__() == 'ni dios ni amo - los olvidados - los muertos de cristo'
