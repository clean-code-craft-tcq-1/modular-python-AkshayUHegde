import wiring_color_code_handler

def test_color_pair_from_pair_number(pair_number, expected_major_color, expected_minor_color):
    major_color, minor_color = wiring_color_code_handler.get_color_pair_from_pair_number(pair_number)
    assert (major_color == expected_major_color)
    assert (minor_color == expected_minor_color)

def test_pair_number_from_color_pair(major_color, minor_color, expected_pair_number):
    pair_number = wiring_color_code_handler.get_pair_number_from_color_pair(major_color, minor_color)
    assert (pair_number == expected_pair_number)
