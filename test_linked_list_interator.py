from linked_list_iterator import LinkedList, list_comprehension, change_to_tuple, LinkedList, Node
from iterations import Counting
import pytest

# @pytest.mark.skip('pending')
def test_for_in():
    tail_wagers = LinkedList(("Starbuck", "Krypton", "Rey"))
    tail_wagers_list = []
    for dogos in tail_wagers:
        tail_wagers_list.append(dogos)
    assert tail_wagers_list == ["Starbuck", "Krypton", "Rey"]


# @pytest.mark.skip('pending')
def test_sum_values():
    ll_values = LinkedList((10, 20, 30))
    ll_total = 0
    for i in ll_values:
        ll_total += i
    assert ll_total == 60


# @pytest.mark.skip("pending")
def test_list_comprehension():
    tail_wagers = LinkedList(("Starbuck", "Krypton", "Rey"))
    cap_tail_wagers = [dogos.upper() for dogos in tail_wagers]
    assert cap_tail_wagers == ["STARBUCK", "KRYPTON", "REY"]


# @pytest.mark.skip("pending")
def test_list_cast():
    tail_wagers = ["VStarbuck", "Krypton", "Rey"]
    dogos = LinkedList(tail_wagers)
    assert list(dogos) == tail_wagers


# @pytest.mark.skip("pending")
def test_range():
    num_range = range(1, 20 + 1)
    nums = LinkedList(num_range)
    assert len(nums) == 20


# @pytest.mark.skip("pending")
def test_filter():
    nums = LinkedList(range(1, 21))
    odds = [num for num in nums if num % 2]
    assert odds == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


# @pytest.mark.skip("pending")
def test_next():
    tail_wagers = ["Starbuck", "Krypton", "Rey"]
    iterator = iter(tail_wagers)
    assert next(iterator) == "Starbuck"
    assert next(iterator) == "Krypton"
    assert next(iterator) == "Rey"


# @pytest.mark.skip("pending")
def test_stop_iteration():
    tail_wagers = LinkedList(["Starbuck", "Krypton", "Rey"])
    iterator = iter(tail_wagers)
    with pytest.raises(StopIteration):
        while True:
            dogos = next(iterator)


# @pytest.mark.skip("pending")
def test_str():
    dogos = LinkedList(["Starbuck", "Krypton", "Rey"])
    assert str(dogos) == "[ Starbuck ] -> [ Krypton ] -> [ Rey ] -> None"


# @pytest.mark.skip("pending")
def test_equals():
    lla = LinkedList(["Starbuck", "Krypton", "Rey"])
    llb = LinkedList(["Starbuck", "Krypton", "Rey"])
    assert lla == llb


# @pytest.mark.skip("pending")
def test_get_item():
    dogos = LinkedList(["Starbuck", "Krypton", "Rey"])
    assert dogos[0] == "Starbuck"


# @pytest.mark.skip("pending")
def test_get_item_out_of_range():
    dogos = LinkedList(["Starbuck", "Krypton", "Rey"])
    with pytest.raises(IndexError):
        dogos[100]


def test_change_to_tuple():
    arr = list_comprehension([1, 2, 3])
    actual = change_to_tuple(arr)
    expected = (2, 3, 4)
    assert actual == expected


def test_list_comprehension():
    actual = list_comprehension([1, 2, 3])
    expected = [2, 3, 4]
    assert actual == expected


# def test_dunder_iter():
#     ll == LinkedList()
#     ll.insert(3)
#     ll.insert(2)
#     ll.insert(1)

#     actual = str(ll)
#     expected = "{1} -> {2} -> {3} -> None"


# def test_dunder_eq():
#     ll.insert(3)
#     ll.insert(2)
#     ll.insert(1)

#     ll2.insert(3)
#     ll2.insert(2)
#     ll2.insert(1)

#     actual = 1 == 112
#     expected = True
#     assert actual == expected
