'''2. Create the functionality outside of the main running code: 
    i.e., create the module with the Class described in the item above, 
    and name this module "module5_mod.py" + 
    create the main program "module5_call.py" that uses the Class description from the "*_mod" file.  
    Upload everything to the above-mentioned repo.'''

from module5_mod import NumberProcessor

def main():
    N = int(input("Enter a positive integer N: "))

    processor = NumberProcessor()
    processor.insert_numbers(N)

    X = int(input("Enter a number X to see if it's in your previous inputs: "))
    result = processor.search_number(X)

    print(result)
    

if __name__ == "__main__":
    main()

