import math

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverege = 5


def paint_calc(height=test_h, width=test_w, cover=coverege):
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"You will neeed {num_of_cans} cans of paint")

paint_calc()