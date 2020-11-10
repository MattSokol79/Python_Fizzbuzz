# FizzBuzz Class

class FizzBuzz:
    def __init__(self):
        # Asks the user to input numbers to represent Fizz and Buzz
        self.fizz = int(input("What number would you like to be 'Fizz'?\n=> "))
        self.buzz = int(input("What number would you like to be 'Buzz'?\n=> "))
        self.fizzbuzz_calculation()

    def fizzbuzz_calculation(self):
        print("OUTPUT\n -> ")
        # Makes sure the range is 1-100 as specified
        for i in range(1, 101):
        # Relevant control flow rules which apply for the numbers in the game
            if i % self.fizz == 0 and i % self.buzz == 0:
                print("FizzBuzz")
            elif i % self.fizz == 0:
                print("Fizz")
            elif i % self.buzz == 0:
                print("Buzz")
            else:
                print(i)
            # Iterate over the process again and again till number 100



# The main function
def main():
    # Testing the functionality by assigning object to class
    test = FizzBuzz()

    # Prints the numbers from 1-100 with FizzBuzz where relevant



# Used to make sure the code is run from the main file
if __name__ == "__main__":
    main()