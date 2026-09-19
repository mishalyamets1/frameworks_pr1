from rooms import add_room, find_room


def test_add_room():
    rooms = {}
    add_room(rooms, "Офис 205", 2, "офис")
    assert len(rooms) == 1
    assert rooms[1]["name"] == "Офис 205"


def test_find_room():
    rooms = {}
    add_room(rooms, "Офис 205", 2, "офис")
    found = find_room(rooms, "офис")
    assert len(found) == 1
    assert found[0]["floor"] == 2
