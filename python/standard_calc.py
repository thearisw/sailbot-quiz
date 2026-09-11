def bound_to_180(angle):
    """Bounds the provided angle between [-180, 180) degrees.

    e.g.)
        bound_to_180(135) = 135.0
        bound_to_180(200) = -160.0

    Args:
        angle (float): The input angle in degrees.

    Returns:
        float: The bounded angle in degrees.
    """

    angle = angle % 360
    if angle >= 180:
        angle -= 360

    return angle


def is_angle_between(first_angle, middle_angle, second_angle):
    """Determines whether an angle is between two other angles.

    e.g.
        is_angle_between(0, 45, 90) = True
        is_angle_between(45, 90, 270) = False

    Args:
        first_angle (float): The first bounding angle in degrees.
        middle_angle (float): The angle in question in degrees.
        second_angle (float): The second bounding angle in degrees.

    Returns:
        bool: True when `middle_angle` is not in the reflex angle of `first_angle` and `second_angle`, false otherwise.
    """

    first_angle = bound_to_180(first_angle)
    middle_angle = bound_to_180(middle_angle)
    second_angle = bound_to_180(second_angle)

    if second_angle < first_angle:
        swap = first_angle
        first_angle = second_angle
        second_angle = swap
    if second_angle - first_angle < 180:
        return first_angle < middle_angle < second_angle
    else:
        return not (first_angle < middle_angle < second_angle)
