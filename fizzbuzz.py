# FizzBuzz Class

class Fizzbuzz:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def fizzbuzz_method(self):
        for i in range(100):
            if i % self.arg1 == 0 and i % self.arg2 == 0:
                return("FizzBuzz")
            elif i % self.arg1 == 0:
                return("Fizz")
            elif i % self.arg2 == 0:
                return("Buzz")
            else:
                return(i)
            i += 1


test = Fizzbuzz(3, 5)

print(test.fizzbuzz_method())
