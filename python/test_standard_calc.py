from standard_calc import bound_to_180, is_angle_between


""" Tests for bound_to_180() """


def test_bound_basic1():
    assert bound_to_180(0) == 0
    assert bound_to_180(180) == -180
    assert bound_to_180(179) == 179
    assert bound_to_180(-180) == -180


def test_bound_over1():
    assert bound_to_180(-181) == 179
    assert bound_to_180(360) == 0
    assert bound_to_180(719) == -1


""" Tests for is_angle_between() """


def test_between_basic1():
    assert is_angle_between(0, 1, 2)
    assert is_angle_between(0, 90, 179)


def test_between_basic2():
    assert not is_angle_between(0, 180, 179)
    assert not is_angle_between(0, 90, 270)


def test_between_basic3():
    assert is_angle_between(0, -1, -90)
    assert is_angle_between(0, -90, 181)


def test_between_overflow():
    assert is_angle_between(0, 1, 362)
    assert not is_angle_between(0, 1, 181)
    assert not is_angle_between(0, 359, 179)
