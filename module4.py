N = int(input("Enter a positive integer N: "))

numbers = []
for i in range(N):
    num = int(input(f"Enter number for {i+1}'s location: "))
    numbers.append(num)

X = int(input("Enter a number X to see if it's in your previous inputs: "))

if X in numbers:
    print(numbers.index(X) + 1)
else:
    print(-1)
