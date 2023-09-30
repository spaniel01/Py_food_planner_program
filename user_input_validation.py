def user_input_validation_int(message, poss_menu_opt_num_max):
        user_input = True
        while user_input == True:
            try:
                user_in = input(message)
                if user_in == "exit":
                     return user_in
                user_in = int(user_in)
                if user_in > 0 and user_in <= poss_menu_opt_num_max:
                    return user_in
                else:
                     int("raising error")
            except:
                print("Please input one of the possible numbers or type 'exit': ")


def user_input_validation_word(message, list_of_words):
        user_input = True
        while user_input == True:
            try:
                user_in = input(message)
                if user_in == "exit":
                     return user_in
                if user_in in list_of_words:
                    return user_in
                else:
                     int("raising error")
            except:
                print("Error! Please type one of the available words or type 'exit':  ")

def user_input_validation_start_of_word(message, list_of_words):
        while True:
            try:
                user_in = input(message)
                if user_in == "exit":
                     return user_in
                for word in list_of_words:
                    if user_in in word:
                        return word
                    else:
                        int("raising error")
            except:
                print("Error! Please type one of the available words or type 'exit':  ")


def user_input_validation_is_number(message):
        user_input = True
        user_in = input(message)
        while user_input == True:
            try:
                if user_in == "exit":
                    return user_in
                user_num = int(user_in)
                return user_num
            except:
                print("Error! Please type a number or type 'exit': ")    

def user_input_validation_y_n(message):
     while True:
        user_in = input(message)
        if user_in == "exit":
            return user_in
        if user_in in ["y", "n"]:
             return user_in
        else:
             print("Incorret input: Please choose between 'y' for yes and 'n' for no!")