from refdatatypes import safedatatypes


def test_safeint():
    assert safedatatypes.safe_int("None") == 0
    assert safedatatypes.safe_int("None", -1) == -1
    assert safedatatypes.safe_int("1") == 1
    assert safedatatypes.safe_int(1) == 1
    assert safedatatypes.safe_int(None, None) is None
    assert safedatatypes.safe_int("", None) is None


def test_safefloat():
    assert safedatatypes.safe_float("None") == 0.0
    assert safedatatypes.safe_float("None", -1.0) == -1.0
    assert safedatatypes.safe_float("1") == 1.0
    assert safedatatypes.safe_float("1.1") == 1.1
    assert safedatatypes.safe_float(1.1) == 1.1
    assert safedatatypes.safe_float(None, None) is None
    assert safedatatypes.safe_float("", None) is None


def test_safebool():
    assert safedatatypes.safe_bool("None") is True
    assert safedatatypes.safe_bool("None", True) is True
    assert safedatatypes.safe_bool("") is False
    assert safedatatypes.safe_bool(1) is True
    assert safedatatypes.safe_bool(0) is False
    assert safedatatypes.safe_bool(None) is False
    assert safedatatypes.safe_bool(None, False) is False


def test_list():
    my_list = safedatatypes.SafeList([1, 2, 3], -1)
    assert my_list[0] == 1
    assert my_list[1] == 2
    assert my_list[2] == 3
    assert my_list[4] == -1


def test_dict():
    my_dict = safedatatypes.SafeDict({"a": 1, "b": 2})
    assert my_dict["a"] == 1
    assert my_dict["b"] == 2
    assert my_dict["c"] is None
    assert str(my_dict) == "{'a': 1, 'b': 2}"


def test_dict2():
    my_dict = safedatatypes.SafeDict({"a": 1, "b": 2}, default_value=-1, autoset=True)
    assert my_dict["a"] == 1
    assert my_dict["b"] == 2
    assert my_dict["c"] == -1
    assert str(my_dict) == "{'a': 1, 'b': 2, 'c': -1}"

def test_dict_recursive():
    my_dict = safedatatypes.SafeDict({"a": 1, "b": {"aa": 1, "bb": 1}})
    assert my_dict["b"]["aa"] == 1
    assert type(my_dict["b"]) == safedatatypes.SafeDict
    assert my_dict.get("c", safedatatypes.SafeDict(), if_none=True).get("cc", -1, if_none=True) == -1
