# FizzBuzz Class

class Fizzbuzz:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def fizzbuzz_method(self, arg1, arg2):
        for i in range(100):
            if i % arg1 == 0 and i % arg2 == 0:
                print("FizzBuzz")
            elif i % arg1 == 0:
                print("Fizz")
            elif i % arg2 == 0:
                print("Buzz")


test = Fizzbuzz(3, 5)

print(test.Fizzbuzz(3, 5))