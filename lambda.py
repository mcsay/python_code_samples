def multiplicition_with_two(x):
    return x * 2

divide_to_three = lambda y : y / 3 # --> same thing with above function

print(int(divide_to_three(15)))


sum = lambda x, y, z : x + y + z

print(int(sum(10,11,12)))


reverse = lambda b : b[::-1]

print(reverse("Python Programming"))


even_odd = lambda t : t % 2 == 0

print(even_odd(10)) # --> True