from .factories import PlayListFactory


def test_str_without_owner_names():
    playlist = PlayListFactory.build(owner__first_name=None, owner__last_name=None)
    assert playlist.__str__() == 'ruido - pity7736@gmail.com'


def test_str_with_owner_names():
    playlist = PlayListFactory.build(owner__first_name='julian', owner__last_name='cortes')
    assert playlist.__str__() == 'ruido - julian cortes'
