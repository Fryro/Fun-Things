import sys

#See Lines 50-52 for an explanation of the factor_amount() function, and where there is a duplicate of it.

def factor_amount(n):
  factors = 1
  counter = 0
  # test_odds_working = "Yes"
  # test_evens_working = "Evens"
  odd_check = 3

  if n % 2 == 0:
    n = n/2
    counter = 0
    factors = 1
    while n % 2 == 0:
      n = n/2
      counter += 1
      factors = 1
      # print(test_evens_working)
      
  factors = factors * (counter + 1)
    
  while n != 1:
    counter = 0
    while n % odd_check == 0:
      n = n/odd_check
      counter += 1
      # print(test_odds_working)
    factors = factors * (counter + 1)
    odd_check += 2
    # test_odds_working = test_odds_working + " Again"
  return factors

##########  This function is used to find the 'index value', or 'N', of a number within TRIANG. TRIANG is the set of all Triangular Numbers, in ascending order, represented by the summation function '1 + 2 + 3 ... N', where N is any positive integer.
##########  This is possible due to the fact that we know each triangular number is equal to :(('N') * ('N + 1') / 2). Since (N) and (N + 1) are consecutive integers, they cannot share prime factors. Thus, we can use the Prime Factorization Theorem to find the total amount of factors a number would have, so long as we exclude one (2^1) from the summation, as only one of the 'N' values can be even.
##########  Any additional comment within this function are for debugging purposes. Simply uncomment the lines to see the total factors calculated in sequence.
def triangular_index(factor_limit):
    n = 1
    number_1 = factor_amount(n)
    number_2 = factor_amount(n + 1)
    while (number_1 * number_2) < target:
        # total_factors = (number_1 * number_2)
        n += 1
        number_1 = number_2
        number_2 = factor_amount(n + 1)
        # print("Total Factors : {}".format(total_factors))
    return n


##########  This is here purely because I wanted the output string to give the amount of factors the number had. Reusing the above 'factor_amount()' will not work due to the fact that it ignores one power of two when calculating factors.
########## This function takes an input value and checks to see if it is even. If it is, it will divide the number by '2' and add '1' to the counter variable. It repeats this until the number is no longer divisble by 2, and then repeats the process for '3', '3+2^1', '3+2^2', and so on, until the number is equal to 1. It then uses an abstraction of the Prime Factorization Theorem to calculate how many factors the input value has.
########## Any additional comments within this function are for debugging purposes. Simply uncomment them all to test the function further.
def factor_amount2(n):
  factors = 1
  counter = 0
  # test_odds_working = "Yes"
  # test_evens_working = "Evens"
  odd_check = 3

  while n % 2 == 0:
    n = n/2
    counter += 1
    factors = 1
    # print(test_evens_working)
      
  factors = factors * (counter + 1)
  counter = 0
    
  while n != 1:
    counter = 0
    while n % odd_check == 0:
      n = n/odd_check
      counter += 1
      # print(test_odds_working)
    factors = factors * (counter + 1)
    odd_check += 2
    # test_odds_working = test_odds_working + " Again"
  return factors

##########  This prints a prompt and gets an input from the user, as well as validate that an input was supplied.
print("Search the set TRIANG, the set of all Real Triangular Numbers, for a value with at least 'X' factors. Please only input values that are integers.")
target = int(input("X = "))
print("Processing...")
##########  This will find the index of the number which satisfies our query.
al_final = triangular_index(target)

##########  This finds the value of that index postion.
final = ((al_final) * (al_final + 1))/2

########## This prints the result and terminates the program.
print("{} is the number occupues the '{}' position of the set TRIANG, and has {} factors. It is the first Triangular Number within the set that has more than {} factors.".format(final, triangular_index(al_final), factor_amount2(final), target))

sys.exit()
