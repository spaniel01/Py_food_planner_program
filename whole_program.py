import copy
from program_setup_load_data_exit_prog import *

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
                print("Please input one of the possible numbers.")


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
                print("Error! Please type one of the available words: ")

def user_input_validation_is_number(message):
        user_input = True
        while user_input == True:
            try:
                user_in = input(message)
                if user_in == "exit":
                     return user_in
                if int(user_in) == int:
                    return user_in
                else:
                     int("raising error")
            except:
                print("Error! Please type one of the available words: ")    

def view_exising_recipes(recipes):
    if len(recipes.keys()) == 0:
        print("There are no recipes yet")
    else:
        counter = 0
        print("These are your current recipes:")
        for key in recipes.keys():
            counter += 1
            print(str(counter) + ". " + key)
        print("----------------")

def show_recipe_ingredients(recipes):
        print("Which recipes' ingredients do you want to see? ")
        view_exising_recipes(recipes)
        recipe_num = input("Please enter a number: ")
        # check input
        counter = 0
        for key in recipes[list(recipes.keys())[int(recipe_num)-1]].keys():
            for key_internal, value in recipes[list(recipes.keys())[int(recipe_num)-1]][key].items():
                if value > 0:
                    counter += 1
                    print(str(counter) + ". " + key_internal + " " + str(value))

### add_recipe
def add_recipe(recipes, ingredients):    
    recipe_name = input("Recipe name: ")
    recipes[recipe_name] = copy.deepcopy(ingredients)
    recipes[recipe_name] = add_recipe_ingredients(recipes[recipe_name])
    return recipes

def add_recipe_ingredients(recipe_):
    print("You can now enter your new ingredients or overwrite exisitng ones. :)")
    recipe_input = True
    while recipe_input == True:
        main_cat = choose_ingredients_main_cat(recipe_)
        recipe_ = add_ingredient_sub_cat(recipe_, main_cat)
        menu_option = input("Edit or add more ingredients? Press enter! \nFinished? Type anything and press enter! ")
        if len(menu_option) == 0:
            continue
        else:
            recipe_input = False 
    return recipe_

def choose_ingredients_main_cat(recipe_, new_recipe = True):
    if new_recipe == True:
        counter = 0
        for key in recipe_.keys():
            counter += 1
            print(str(counter) + ". " + key)
        menu_option = user_input_validation_int("Input your desired food type: ", counter)
        return list(recipe_.keys())[menu_option-1]

def add_ingredient_sub_cat(recipe_, main_cat):
    counter = 0
    for key in recipe_[main_cat].keys():
        counter += 1
        print(str(counter) + ". " + key)
    minor_cat_number = user_input_validation_int("Input your desired ingredient: ", counter)
    quantity = user_input_validation_is_number("Input your desired quantity (in grams or units): ")
    recipe_[main_cat][list(recipe_[main_cat].keys())[int(minor_cat_number)-1]] = int(quantity)
    return recipe_
### add_recipe() end

def show_recipe_ingredients(recipes):
        print("Which recipes' ingredients do you want to see? ")
        view_exising_recipes(recipes)
        recipe_num = input("Please enter a number: ")
        # check input
        counter = 0
        for key in recipes[list(recipes.keys())[int(recipe_num)-1]].keys():
            for key_internal, value in recipes[list(recipes.keys())[int(recipe_num)-1]][key].items():
                if value > 0:
                    counter += 1
                    print(str(counter) + ". " + key_internal + " " + str(value))

def edit_recipe(recipes):
     if len(recipes.keys()) > 0: 
        print("These are you current recipes:")
        view_exising_recipes(recipes)
        user_in = user_input_validation_int("Which recipe would you like to edit? Please input the corresponding number: ", len(recipes.keys()))
        # convert to integer, check input and adjust show_recipe_ingredients
        print(user_in, recipes.keys())
        recipe_name = list(recipes.keys())[user_in-1]
        print("This is the recipe you want to edit: " + recipe_name)
        counter = 0
        for key in recipes[recipe_name].keys():
            for key_internal, value in recipes[recipe_name][key].items():
                if value > 0:
                    counter += 1
                    print(str(counter) + ". " + key_internal + " " + str(value))
        # user input check
        editing_recipe = True
        while editing_recipe == True:
            user_in = user_input_validation_int("What would you like to edit:\n1. The recipe name\n2. Add or overwrite recipe ingredients\n3. Delete an ingredient\n4. Return to the main menu", 4)
            if user_in == 1:
                new_recipe_name = input("What should the new name of the recipe be?")
                recipe_ingredients_dict = recipes[recipe_name].copy()
                recipes[new_recipe_name] = recipe_ingredients_dict
                del recipes[recipe_name]
                recipe_name = new_recipe_name
            elif user_in == 2:
                recipes = add_recipe_ingredients(recipes[recipe_name])
            elif user_in == 3:
                print("These are the current ingredients:")
                counter = 0
                print("REC ", recipe_name)
                for key in recipes[recipe_name].keys():
                    print("REC ",1)
                    for key_internal, value in recipes[recipe_name][key].items():
                        print("REC ",2)
                        if value > 0:
                            counter += 1
                            print(str(counter) + ". " + key_internal + " " + str(value))
                word_list = []
                for key in recipes[recipe_name].keys():
                    for key_internal in recipes[recipe_name][key].keys():
                        word_list.append(key_internal)
                user_in = user_input_validation_word("Which ingredient would you like to delete? Please type the name of the ingredient: ", word_list)
                for key in recipes[recipe_name].keys():
                    for key_internal, value in recipes[recipe_name][key].items():
                        if key_internal == user_in:
                            key_for_deletion = key
                            print(recipes[recipe_name][key][key_internal], " deleted")
                recipes[recipe_name][key_for_deletion][user_in] = 0
            elif user_in == 4:
                return recipes
            else:
                print("Unexpected error: 2")
     else:
        return None

def delete_recipe(recipes):
    view_exising_recipes(recipes)
    user_in = input("Which recipe would you like to delete? Please input the corresponding number. To return to the main menu, type main press enter.")
    if len(user_in) == 0:
        pass #return to main
    else:
        recipes.pop(recipes[recipes.keys()[user_in]-1])
    return recipes
