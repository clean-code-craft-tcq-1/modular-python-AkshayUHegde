import test

if __name__ == '__main__':
    test.test_color_pair_from_pair_number(4, 'White', 'Brown')
    test.test_color_pair_from_pair_number(5, 'White', 'Slate')
    test.test_pair_number_from_color_pair('Black', 'Orange', 12)
    test.test_pair_number_from_color_pair('Violet', 'Slate', 25)
    test.test_pair_number_from_color_pair('Red', 'Orange', 7)
    print('Done :)')
