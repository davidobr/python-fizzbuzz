class FizzBuzz:
    value = ""

    def __init__(self):
        for i in range(1, 101):
            if i % 3 == 0 and i % 5 == 0:
                value = "fizzbuzz"
                print(value)
            elif i % 3 == 0:
                value = "fizz"
                print(value)
            elif i % 5 == 0:
                value = "buzz"
                print(value)
            else:
                value = i
                print(value)


fb = FizzBuzz()
print(fb)
