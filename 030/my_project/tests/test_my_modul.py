from src.my_modul import addiere, ist_gerade


def test_addiere():
    assert addiere(2, 3) == 5
    assert addiere(-1, 1) == 0


def test_ist_gerade():
    assert ist_gerade(4) is True
    assert ist_gerade(5) is False
