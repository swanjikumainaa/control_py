
# Write a function that uses while, if and continue statements
#  to print all the even numbers between 0 and 50. 

def even_numbers():
    num = 0
    while num <= 50:
        if num % 2 == 0:
            print(num)
        num += 1
        continue

# Write a function that takes an integer argument and 
# prints "Prime" if the number is prime, and "Not prime" if the number is not prime.
def is_prime():
    if x < 2:
        print("Not prime")
        return
    
    for i in range(2):
        if x % i == 0:
            print("Not prime")
            return
    
    print("Prime")

 # Write a function that takes a list of integers as input and prints
 #  the sum of all the even numbers in the list.  
def sum_even_numbers(numbers):
    sum = 0
    for num in numbers:
        if num % 2 == 0:
            sum += num
    print(sum)



# Write a function that takes any two integers as input, and prints
#  the sum of all the numbers between the two integers (inclusive) that are divisible by 3.
def sum_divisible_by_3():
    sum = 0
    for num in range():
        if num % 3 == 0:
            sum += num
    print(sum)
