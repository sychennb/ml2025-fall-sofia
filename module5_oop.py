'''1. Create a Python program:

The program asks the user for input N (positive integer) and reads it

Then the program asks the user to provide N numbers (one by one) and reads all of them (again, one by one)

In the end, the program asks the user for input X (integer) and outputs: "-1" if there were no such X among N read numbers, or the index (from 1 to N) of this X if the user inputted it before.

The basic functionality of data processing (data initialization, data insertion, data search) should be done via Object-Oriented Programming Paradigm (i.e. using Classes)

Name this program "module5_oop.py" and upload it to the above-mentioned repo.'''

class NumberProcessor:
    def __init__(self):
        self.numbers = []

    def insert_numbers(self, n):
        for i in range(n):
            num = int(input(f"Enter number for {i + 1}'s location: "))
            self.numbers.append(num)

    def search_number(self, x):
        if x in self.numbers:
            return self.numbers.index(x) + 1
        else:
            return -1


def main():
    N = int(input("Enter a positive integer N: "))

    processor = NumberProcessor()
    processor.insert_numbers(N)

    X = int(input("Enter a number X to see if it's in your previous inputs: "))
    result = processor.search_number(X)

    print(result)


if __name__ == "__main__":
    main()
