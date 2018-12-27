# Example of Iterator Design Pattern


def count_to(count):
    numbers = ["one", "two", "three", "four", "five"]
    for number in numbers[:count]:
        yield number


count_to_two = count_to(2)
count_to_five = count_to(5)

for count in [count_to_two, count_to_five]:
    for number in count:
        print(number, end=' ')
    print()
