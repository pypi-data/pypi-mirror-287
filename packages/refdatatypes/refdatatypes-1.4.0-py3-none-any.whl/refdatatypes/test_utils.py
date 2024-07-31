from refdatatypes.utils import dict_item_must_be_list


def test_must_be_list():
    d = {"a": 1, "b": {"bb": 22}}
    dict_item_must_be_list(d, "b.bb")
    assert d["b"]["bb"] == [22]


def test_must_be_list_2():
    d = {"a": 1, "b": {"bb": [{"ccc": 1, "ddd": 2}, {"ccc": [2, 3], "ddd": 2}, {"ccc": 4, "ddd": 2}]}}
    dict_item_must_be_list(d, "b.bb.ccc")
    assert d["b"]["bb"][0]["ccc"] == [1]
    assert d["b"]["bb"][0]["ddd"] == 2
    assert d["b"]["bb"][1]["ccc"] == [2, 3]
    assert d["b"]["bb"][1]["ddd"] == 2
    assert d["b"]["bb"][2]["ccc"] == [4]
    assert d["b"]["bb"][1]["ddd"] == 2


def test_must_be_list_3():
    d = {
        "a": 1,
        "b": {
            "bb": [
                {"ccc": {"ddd": 4}},
                {"ccc": [{"ddd": 4}, {"ddd": 4}]},
                {"ccc": 4},
                {"ccc": None},
                {"ccc": [1, 2, [11, 22]]},
            ]
        },
    }
    dict_item_must_be_list(d, "b.bb.ccc")
    assert d["b"]["bb"][0]["ccc"] == [{"ddd": 4}]
    assert d["b"]["bb"][1]["ccc"] == [{"ddd": 4}, {"ddd": 4}]
    assert d["b"]["bb"][2]["ccc"] == [4]
    assert d["b"]["bb"][3]["ccc"] == []
    assert d["b"]["bb"][4]["ccc"] == [1, 2, [11, 22]]
