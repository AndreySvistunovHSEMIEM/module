from algorithms.sort import merge_sort


def test_sorted():
    assert merge_sort([3, 1, 4, 1, 5, 9]) == [1, 1, 3, 4, 5, 9]


def test_empty():
    assert merge_sort([]) == []


def test_single():
    assert merge_sort([1]) == [1]


def test_already_sorted():
    assert merge_sort([1, 2, 3]) == [1, 2, 3]


def test_reverse():
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_does_not_mutate():
    original = [3, 1, 2]
    merge_sort(original)
    assert original == [3, 1, 2]
