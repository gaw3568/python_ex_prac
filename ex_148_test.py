

def test_ex_148():
    list = ex.Get_csv("User_info.csv")
    assert list is not None
    assert list.count == 10



