## This is used exclusively for checking stocks, at the end of the program. You may change this as you see fit.
manager_password = "banana"

## 'While' loop that ensures integrity of user input.
salad_count = ""
while (salad_count == ""):
    try:
        salad_count = int(input("Welcome to Salads 'R Us!\n\t Enter how many salads you would like : "))
    except:
        print("Something went wrong. Restarting...")
        salad_count = ""
        
## Overall program boolean
running = True

## Stock Dict
stock_dict = {"ROMAINE":0, "SPRING_MIX":0, "ARUGALA":0, "KALE":0, "TOMATO":0, "CUCUMBER":0, "CRANBERRY":0, "CHEDDAR_CHEESE":0, "FETA_CHEESE":0, "BLUE_CHEESE":0, "BACON":0, "CROUTONS":0, "SUNFLOWER_SEEDS":0, "WALNUTS":0, "ONIONS":0, "OLIVES":0, "BELL_PEPPERS":0, "ITALIAN":0, "RANCH":0, "FRENCH":0, "DONE":0, "CANCEL":0}
## Stock Dict (Total vs Used)
in_stock = {"ROMAINE":{"72":0}, "SPRING_MIX":{"120":0}, "ARUGALA":{"72":0}, "KALE":{"120":0}, "TOMATO":{"168":0}, "CUCUMBER":{"200":0}, "CRANBERRY":{"150":0}, "CHEDDAR_CHEESE":{"300":0}, "FETA_CHEESE":{"120":0}, "BLUE_CHEESE":{"90":0}, "BACON":{"300":0}, "CROUTONS":{"240":0}, "SUNFLOWER_SEEDS":{"120":0}, "WALNUTS":{"90":0}, "ONIONS":{"500":0}, "OLIVES":{"300":0}, "BELL_PEPPERS":{"250":0}, "ITALIAN":{"300":0}, "RANCH":{"300":0}, "FRENCH":{"300":0}, "DONE":{"0":0}, "CANCEL":{"0":0}}
price_dict = {"ROMAINE":60.00, "SPRING_MIX":16.74, "ARUGALA":66.00, "KALE":6.60, "TOMATO":288, "CUCUMBER":26.4, "CRANBERRY":35.28, "CHEDDAR_CHEESE":48.00, "FETA_CHEESE":51.00, "BLUE_CHEESE":234.00, "BACON":132.00, "CROUTONS":60.00, "SUNFLOWER_SEEDS":111.00, "WALNUTS":96.00, "ONIONS":28.00, "OLIVES":24.00, "BELL_PEPPERS":89.75, "ITALIAN":18.00, "RANCH":12.00, "FRENCH":9.86, "DONE":0.00, "CANCEL":0.00}

    
## Function that resets the values of key,value pairs for each ingredient category.
def reset_salad_dicts():
    greens_dict = {"ROMAINE":0, "SPRING_MIX":0, "ARUGALA":0, "KALE":0, "DONE":0, "CANCEL":0}
    healthy_dict = {"TOMATO":0, "CUCUMBER":0, "CRANBERRY":0, "DONE":0, "CANCEL":0}
    cheese_dict = {"CHEDDAR_CHEESE":0, "FETA_CHEESE":0, "BLUE_CHEESE":0, "DONE":0, "CANCEL":0}
    crunchy_dict = {"BACON":0, "CROUTONS":0, "SUNFLOWER_SEEDS":0, "WALNUTS":0, "DONE":0, "CANCEL":0}
    extra_dict = {"ONIONS":0, "OLIVES":0, "BELL_PEPPERS":0, "DONE":0, "CANCEL":0}
    dressings_dict = {"ITALIAN":0, "RANCH":0, "FRENCH":0, "DONE":0, "CANCEL":0}
    
    
    
    
## Prints key,value pairs in a dictionary.
def print_dict(dictionary):
    for key,value in dictionary.items():
        print("Choice : {}\n\tAmount : {}".format(key, value))

## A function designed to get valid user inputs.
def get_input():
    temp_run_input = True
    while temp_run_input:
        try:
            input_var = input("*****\nPlease enter a choice : ")
            temp_run_input = False
        except Exception as e:
            print("Invalid input. \nError Encountered : {}".format(e))
    if (input_var == ""):
        return("DONE")
    return input_var
    
## If the user wishes to cancel their order, this function provides that precaution.
def cancel_prompt():
    cancel_status = int(input("Are you sure you would like to cancel your order?\n1: Cancel order\n2: Continue order\n\t Enter : "))
    if (cancel_status == 1):
        print("Cancelling order...")
        running = False
    elif (cancel_status == 2):
        print("Continuing order...")
    else:
        print("Invalid input. Continuing order...")
        
## This takes a dictionary and runs an input against the keys in it.
def ask_item(dictionary):
    temp_run_ask = True
    valid_temp = "Cancel"
    while (temp_run_ask):
        ## Adds keys to a string of valid inputs
        for key,value in dictionary.items():
            valid_temp += (" " + key.lower())
        final_var = get_input()
        ## If input in valid input string...
        if (final_var.lower() in valid_temp):
            ## If cancel...
            if (final_var.lower() == "cancel"):
                cancel_prompt()
            ## If done...
            if (final_var.lower() == "done"):
                return final_var.upper()
            ## If neither AND valid...
            else:
                return final_var.upper()
                temp_run_ask = False
        else:
            print("***\nPlease enter a valid input\n***")
            temp_run_ask = True
            
## This takes a dictionary, an ingredient category, and a salad number. It will then ask for ingredients in that dictionary, calling the other integrity-assuring functions, until the user cancels the order or indicates they are finished with that ingredient category.
def driver_ask(dictionary, category, salad):
    final_temp = True
    while final_temp:
        final_choice = ask_item(dictionary)
        ## If input in dictionary in keys AND not equal to 1, increment by 1
        if (final_choice in dictionary.keys()):
            if (dictionary[final_choice] != 1):
                dictionary[final_choice] += 1
            ## If already one...
            else:
                print("You have already selected this as a topping.")
        ## If not in keys...
        else:
            print("Please select a valid topping.")
        ## Dictionary Parsings
        for key,value in dictionary.items():
            if (value > 0):
                if (key != "DONE"):
                    print("You have selected {} serving(s) of {} in salad {}".format(value, key, salad))
        ## If input is DONE... (exits menu)
        if (final_choice == "DONE"):
            print("You have finished {} selections for : Salad {}".format(category, salad))
            final_temp = False
        ## If input is CANCEL
        if (final_choice == "CANCEL"):
            cancel_prompt()
            
## Main iterative loop
while (running):
    init_run = True
    print("*****\nAt any input, you may enter 'Cancel' to cancel your order.\n*****")
    
    ## Start of Salad Iteration
    for i in range(salad_count):
        ## Initializes blank dictionaries
        greens_dict = {"ROMAINE":0, "SPRING_MIX":0, "ARUGALA":0, "KALE":0, "DONE":0, "CANCEL":0}
        healthy_dict = {"TOMATO":0, "CUCUMBER":0, "CRANBERRY":0, "DONE":0, "CANCEL":0}
        cheese_dict = {"CHEDDAR_CHEESE":0, "FETA_CHEESE":0, "BLUE_CHEESE":0, "DONE":0, "CANCEL":0}
        crunchy_dict = {"BACON":0, "CROUTONS":0, "SUNFLOWER_SEEDS":0, "WALNUTS":0, "DONE":0, "CANCEL":0}
        extra_dict = {"ONIONS":0, "OLIVES":0, "BELL_PEPPERS":0, "DONE":0, "CANCEL":0}
        dressings_dict = {"ITALIAN":0, "RANCH":0, "FRENCH":0, "DONE":0, "CANCEL":0}

        ## Creates a list of the above dictionaries
        dict_list = [greens_dict, healthy_dict, cheese_dict, crunchy_dict, extra_dict, dressings_dict]
        
        ## Driver Code for Greens Selection
        print("We will now ask for the greens you would like in salad {}.".format(str(i+1)))
        print_dict(greens_dict)
        driver_ask(greens_dict, "greens", i+1)
                
        ## Driver Code for Healthy Toppings Selection
        print("We will now ask for the healthy toppings you would like in salad {}.".format(str(i+1)))
        print_dict(healthy_dict)    
        driver_ask(healthy_dict, "healthy toppings", i+1)
        
        ## Driver Code for Cheese Selection
        print("We will now ask for the cheeses you would like in salad {}.".format(str(i+1)))
        print_dict(cheese_dict)    
        driver_ask(cheese_dict, "cheeses", i+1)
        
        ## Driver Code for Crunchy Selection
        print("We will now ask for the crunchy items you would like in salad {}.".format(str(i+1)))
        print_dict(crunchy_dict)    
        driver_ask(crunchy_dict, "crunchy items", i+1)
        
        ## Driver Code for Extras Selection
        print("We will now ask for the extra toppings you would like in salad {}.".format(str(i+1)))
        print_dict(extra_dict)    
        driver_ask(extra_dict, "extra items", i+1)
        
        ## Driver Code for Dressings Selection
        print("We will now ask for the dressings you would like in salad {}.".format(str(i+1)))
        print_dict(dressings_dict)    
        driver_ask(dressings_dict, "dressing items", i+1)
        
        
        print("\n\n===\nSALAD {} SUMMARY\n===".format(str(i+1)))
        ## Dict Parsing
        for dictionary in dict_list:
            for key,value in dictionary.items():
                if (value > 0):
                    if (key != "DONE"):
                        print("You have selected {} servings of {} in salad {}.".format(value, key, str(i+1)))
        
        ## GUI
        print("=====\nEnter TRUE or FALSE : Is this correct?\n=====")
        confirmation = get_input()
        ## Confirms the items and records items for stock use. Then resets for future use.
        if (confirmation.upper() == "TRUE"):
            for dictionary in dict_list:
                for key,value in dictionary.items():
                    if (value > 0):
                        if ((key != "DONE") and (key != "CANCEL")):
                            stock_dict[key] += 1
            print("Salad {} finalized.".format(str(i+1)))

        ## Cancels the Salad and RESETS THE DICTIONARIES    
        elif (confirmation.upper() == "FALSE"):
            reset_salad_dicts()
            print("Salad {} cancelled.".format(str(i+1)))
        ## If Confirmation returns an invalid input...
        else:
            ## Dict Parsing, if value > 0, and not DONE/CANCEL...
            for dictionary in dict_list:
                for key,value in dictionary.items():
                    if (value > 0):
                        if ((key != "DONE") and (key != "CANCEL")):
                            ## Increment stocks by 1
                            stock_dict[key] += 1
            print("Invalid input. Finalizing Salad by Default.")
        
        ## GUI
        print("===")
        ## For each dictionary in dict_list, then Dict Parsing...
        for dictionary in dict_list:
            for key,value in dictionary.items():
                ## If value > 0
                if (value > 0):
                    ## If NOT DONE or CANCEL
                    if ((key != "DONE") and (key != "CANCEL")):
                        ## Expanded (SWITCH : CASE) which increments amounts used based on ingredients used.
                        if (key in greens_dict.keys()):
                            value *= 3
                            print("Your salad will include {} cups of {}.".format(str(value), key))
                        elif ((key == ("TOMATO")) or (key == ("CUCUMBER"))):
                            value *= 5
                            if (key == "TOMATO"):
                                print("Your salad will include {} GRAPE TOMATOES.".format(str(value)))
                            if (key == "CUCUMBER"):
                                print("Your salad will include {} servings of CUCUMBER.".format(str(value)))
                        elif (key in cheese_dict.keys()):
                            value *= 0.5
                            print("Your salad will include {} ounces of {}.".format(str(value), key))
                        elif (key in dressings_dict.keys()):
                            value *= 4
                            print("Your salad will include {} ounces of {}.".format(str(value), key))
                        else:
                            print("Your salad will include {} ounces of {}.".format(str(value), key))
                    ## Dict Parsing
                    for ingredient,ratio in in_stock.items():
                        ## If key == ingredient, isn't DONE or CANCEL...
                        if (key == ingredient):
                            if ((key != "DONE") and (key != "CANCEL")):
                                ## Dict Parsing
                                for stocked,used in ratio.items():
                                    ratio[stocked] += 1
        ## Reset TempDicts for next iteration
        reset_salad_dicts()
    running = False
    
## This function checks the stocked vs used dictionary and prints outputs
def stock_check():
    print("Checking stocks...")
    ## Dictionary Iteration
    for ingredient,ratio in in_stock.items():
        for stocked,used in ratio.items():
            ## If used > 0...
            if (used > 0):
                ## If 2/3rds of stock used or more...
                if ((int(stocked) - used) <= (int(stocked) / 3)):
                    print("****====****\nOrder a new shipment of {}. There are {} servings remaining of {} total.\n\tThis will cost ${}.\n****====****".format(ingredient, (int(stocked) - used), stocked, price_dict[ingredient]))
            ## If used not greater than 0...
            else:
                print("--\nYou do not need a new shipment of {}. There are {} servings remaining of {} total.\n\tA new shipment would cost : ${}.".format(ingredient, (int(stocked) - used), stocked, price_dict[ingredient]))

## Error Handling and User Input Collection
stock_temp = ""
try:
    stock_temp = input("====\n\nEnter the manager's password to enter the Stock Menu. Any other input WILL NOT enter the Stock Menu.\n\tEnter : ")
except:
    print("Invalid input. Stocks will not be checked.")
    
## If password entered...
if (stock_temp == manager_password):
    ## GUI and User Input Collection
    print("====\nEntering Stock Menu...\n====")
    stock_q = ""
    while (stock_q == ""):
        try:
            stock_q = input("--\n1: Search a Specific Stock\n2: Print all Stocks\nAny other input: Exit Stock Menu\n\tEnter your selection here : ")
        except:
            print("Invalid input.")
            stock_q = ""
    
        ## If "1" is input...
        if (stock_q == "1"):
            query = input("\tPlease enter an ingredient : ")
            for ingredient,ratio in in_stock.items():
                if (query.upper() == ingredient):
                    print("=-=\n['Starting Stock' : Used]\n{}\n\tPrice of new stock : ${}\n=-=".format(in_stock[ingredient], price_dict[ingredient]))
            stock_q = ""
        ## If "2" is input...
        elif (stock_q == "2"):
            stock_check()
            stock_q = ""
        ## If not "1" or "2"...
        else:
            print("Exiting Stock Menu...")
            stock_q = "EXIT_CONDITION"
