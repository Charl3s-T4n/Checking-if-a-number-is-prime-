#Write your code below this line 👇
#Method 1: Using for else with break statement 
def prime_checker(number):
  if number > 1:
    for num in range(2,number):
      if number % num == 0:
        print("It's not a prime number.")
        break
    else:
      print("It's a prime number.")
  else:
    print("It's not a prime number.")

    
#Method 2: Using flag variable 
def prime_checker(number):
  is_prime = True
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



