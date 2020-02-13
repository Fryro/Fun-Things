## Programs 5, 4, 2, and 1 use the same basic structure.
## They first create an empty counter, base_counter, and base_list
## They then iterate through their upper required bound, checking the counter against the requirements of the program, incrementing the base_counter and appending counter to the base_list if it matches the requirements.
## It then increments the counter variable.
## Finally, it will print the amount of numbers that matched the requirements, and then print the required output.

## Program 1
def program_1():
  counter = 0
  even_counter = 0
  even_list = []
  while (counter < 101):
    if ((counter % 2) == 0):
      even_counter += 1
      even_list.append(counter)
    counter += 1
  print("Even numbers between 0 and 100...\n\t Count : {} \n\t Numbers : {}\n\n".format(even_counter, even_list))

## Program 2 
def program_2():
  counter = 0
  fives_counter = 0
  fives_list = []
  while (counter < 101):
    if ((counter % 5) == 0):
      fives_counter += 1 
      fives_list.append(counter)
    counter += 1
  print("Numbers divisible by 5 between 0 and 100. \n\t Count : {} \n\t Numbers : {}\n\n".format(fives_counter, fives_list))

## Program 3
def program_3():
  sports_list = []
  rank_list = ["1st", "2nd", "3rd"]
  ## Driver Code
  for i in range(3):
    ## Asks question and appends answer to a list.
    sports_list.append(input("Please enter your {} favourite sport : ".format(rank_list[i])))
  ## Prints Answers
  print("Your favourite sports are : {}\n\n".format(sports_list))


## Program 4
def program_4():
  counter = 0
  odd_counter = 0
  odd_list = []
  running_total = 0
  while (counter <= 100):
    if ((counter % 2) != 0):
      odd_counter += 1
      odd_list.append(counter)
    counter += 1
  for number in odd_list:
    running_total += number
  print("The sum of all odd numbers between 0 and 100. \n\t Amount of Numbers : {} \n\t Total Sum : {}\n\n".format(odd_counter, running_total))

## Program 5
def program_5():
  counter = 0
  even_counter = 0
  product_variable = 0
  even_list = []
  while (counter <= 100):
    if ((counter % 2) == 0):
      if (counter == 0):
        product_variable += 1
      else:
        even_counter += 1
        even_list.append(counter)
    counter += 1
  for number in even_list:
    product_variable *= number
    #print(product_variable) ## Debug Print
  print("The product of all even numbers between 1 and 50. \n\t Amount of Numbers : {} \n\t Total Product : {}\n\n".format(even_counter, product_variable))

## Program 6
def program_6():
## Sets secret colour
  secret_colour = input("Input a colour for the next user to guess : ")
  guess = ""
  initial_run = True
  ## Code that checks guess against secret_colour
  while (guess.lower() != secret_colour.lower()):
    if (initial_run):
      guess = input("Guess the previous user's secret colour : ")
      initial_run = False
    else:
      print("That was incorrect.")
      guess = input("Guess a colour : ")
  ## Checks if user guessed correctly
  if (guess.lower() == secret_colour.lower()):
    print("Congratulations! The colour was : {}".format(secret_colour))

## Program 7
def program_7():
  ## List of Questions
  questions_list = ["What is your favourite colour?", "What is your favourite animal?", "What is your favourite number?", "What is your favourite place to be?", "Where is your least favourite place to be?"]
  ## List of Follow-Up Questions
  secondary_questions_list = ["Why is that your favourite?", "What is one memory you have involving that?"]
  answer_list = []
  answer_list2 = []
  ## Asks Questions and gets Primary Answers
  for question in questions_list:
    print(question)
    answer_temp = input("\t\tEnter your answer here : ")
    answer_list.append(answer_temp)
  ## Shows the user their answers
  for i in range(5):
    print("{}\n\t\t\t You answered : {}".format(questions_list[i], answer_list[i]))
    ## If question 2, 4, or 1...
    if ((i == 1) or (i == 3) or (i == 0)):
      ## Ask follow up question
      for question in secondary_questions_list:
        print(question)
        ## Gets answer and shows it to the user
        answer_temp = input("\t\tEnter your answer here : ")
        answer_list2.append(answer_temp)
        print("\t\t\t You answered : {}".format(answer_temp))

## Program 8
def program_8():
  scores_list = []
  average = 0
  legal_inputs = ""
  ## Creating legal inputs
  for i in range(251):
    legal_inputs += (" " + str(i))
  #print(legal_inputs) ## Debug print
  ## Driver Code
  for i in range(10):
    ## Temporarily sets temp_score to -1 for primary iteration
    temp_score = -1
    ## Checks if input is legal
    while (str(temp_score) not in legal_inputs):
      ## Pythonic Error Resolution
      try:
        temp_score = int(input("Please enter an integer between 0 and 250.\n\t Enter score [{}]/[{}] : ".format(str(i+1), str(10))))
      except:
        print("That is not a legal input.")
    scores_list.append(temp_score)
  ## Creates/Calculates/Prints Average
  for score in scores_list:
    average += score
  average = average / 10
  print("The average of the scores was : {}\n\t The scores were : {}".format(average, scores_list))
