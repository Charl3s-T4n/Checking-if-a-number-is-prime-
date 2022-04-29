#Write your code below this line 👇
#Method 1: Using for else with break statement 
def prime_checker(number):
  if number > 1:
    for num in range(2,number):               # Exclude 1 and number 
      if number % num == 0:                   # If the number can be evenly divided by a number between 1 and the number itself: not prime
        print("It's not a prime number.")
        break                                # Allows me to exit out of 'for' loop when 'if' condition is True: Hence only print that statement once 
    else:                                  # Same indent as 'for' loop: 'else' will be executed only if a 'break' statement not encountered in 'for' loop
      print("It's a prime number.")
  else:                                         # Numbers that are <1 are not prime 
    print("It's not a prime number.")

    
#Method 2: Using flag variable 
def prime_checker(number):
  is_prime = True                   # Create flag variable 
  for num in range(2,number):
    if number % num ==0:
      is_prime = False
  if is_prime:                    #if is_prime = True
    print("It's a prime number.")
  else:                           #if is_prime = False
    print("It's not a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



