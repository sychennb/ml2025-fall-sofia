'''2. Create the functionality outside of the main running code: 
    i.e., create the module with the Class described in the item above, 
    and name this module "module5_mod.py" + 
    create the main program "module5_call.py" that uses the Class description from the "*_mod" file.  
    Upload everything to the above-mentioned repo.'''

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
