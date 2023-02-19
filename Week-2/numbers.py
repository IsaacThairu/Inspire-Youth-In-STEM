#write a program to list all odd numbers from 1-100
for odd_numbers in range(1,100):
    if (odd_numbers%2 !=0):
        print(odd_numbers)
        
#write a program to list all prime numbers from 1-100
for prime_numbers in range(1,100):
    if prime_numbers >1:
        for i in range (1,100):
            if (prime_numbers% i) == i:
                print(prime_numbers)


        
