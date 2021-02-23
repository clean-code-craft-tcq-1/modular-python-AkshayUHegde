import wiring_color_code_handler

def print_color_code_reference():
    row_format = "{:>15}" * (3)
    table_headers = ["Pair number", "Major Color", "Minor Color"]
    print(row_format.format("","25-Pair Color Code",""))
    print(row_format.format(*table_headers))
    for i in range(1, 25):
        color_pair = wiring_color_code_handler.get_color_pair_from_pair_number(i)
        print(row_format.format(i, *color_pair))

if __name__ == '__main__':
    print_color_code_reference()