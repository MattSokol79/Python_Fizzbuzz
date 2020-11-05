# FizzBuzz Class

class Fizzbuzz:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def fizzbuzz_method(self):
        arg1 = int(input("What number would you like to assign to Fizz? "))
        arg2 = int(input("What number would you like to assign to Buzz? "))

        for i in range(101):

            if i % arg1 == 0 and i % arg2 == 0:
                print("FizzBuzz")
            elif i % arg1 == 0:
                print("Fizz")
            elif i % arg2 == 0:
                print("Buzz")
            else:
                print(i)
            i += 1


test_1 = Fizzbuzz(3, 5)

print(test_1.fizzbuzz_method())
