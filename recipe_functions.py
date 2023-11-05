import copy
import user_input_validation as u_i_v
import numpy as np

def view_exising_recipes(recipes):
    if len(recipes.keys()) == 0:
        print("There are no recipes yet")
        no_recipe = True
        return no_recipe
    else:
        counter = 0
        print("These are your current recipes:")
        for key in recipes.keys():
            counter += 1
            print(str(counter) + ". " + key)
        no_recipe = False
        return no_recipe

def show_recipe_ingredients(recipes):
        print("Which recipe's ingredients do you want to see? ")
        no_recipe = view_exising_recipes(recipes)
        if no_recipe == False:
            recipe_num = u_i_v.user_input_validation_int("Please enter a number: ", len(recipes.keys()))
            if recipe_num == "exit":
                return recipes
            counter = 0
            for key in recipes[list(recipes.keys())[int(recipe_num)-1]].keys():
                for key_internal, value in recipes[list(recipes.keys())[int(recipe_num)-1]][key].items():
                    if value > 0:
                        counter += 1
                        print(str(counter) + ". " + key_internal + ", " + str(value))
        if counter == 0:
            print("This recipe has no ingredients to show!")

### add_recipe
def add_recipe(recipes, ingredients):    
    recipe_name = input("Recipe name: ")
    if recipe_name == "exit":
        return recipes
    recipes[recipe_name] = copy.deepcopy(ingredients)
    add_recipe_ingredient_out = add_recipe_ingredients(recipes[recipe_name])
    if add_recipe_ingredient_out == "exit":
        return recipes
    recipes[recipe_name] = add_recipe_ingredient_out
    return recipes

def create_edit_reg_shopping_list(reg_shopping_list, ingredients): 
    while True:
        for key in ingredients.keys():
            counter += 1
            print(str(counter) + ". " + key)
        main_cat = u_i_v.user_input_validation_int("Input your desired food type (as a number): ", counter)
        if main_cat == "exit":
            return reg_shopping_list    
        counter = 0
        for key in ingredients[main_cat].keys():
            counter += 1
            print(str(counter) + ". " + key)
        minor_cat_number = u_i_v.user_input_validation_int("Input your desired ingredient (as a number): ", counter)
        if minor_cat_number == "exit":
            return reg_shopping_list
        quantity = u_i_v.user_input_validation_is_number("Input your desired quantity (in grams or units): ")
        if quantity == "exit":
            return reg_shopping_list
        reg_shopping_list[main_cat][list(ingredients[main_cat].keys())[int(minor_cat_number)-1]] = int(quantity)    
        return reg_shopping_list

def add_recipe_ingredients(recipe_):
    print("You can now enter your new ingredients or overwrite exisiting ones.\nIf you want to 'delete' an ingredient, just set the quantity to 0.\nIf you want to return to the main menu, type 'exit'. :)")
    recipe_input = True
    while recipe_input == True:
        main_cat = choose_ingredients_main_cat(recipe_)
        if main_cat == "exit":
            return recipe_
        recipe_ = add_ingredient_sub_cat(recipe_, main_cat)
        if recipe_ == "exit":
            return recipe_
        menu_option = input("Edit or add more ingredients? Press enter! \nFinished? Type anything and press enter! ")
        if menu_option == "":
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
        menu_option = u_i_v.user_input_validation_int("Input your desired food type (as a number): ", counter)
        if menu_option == "exit":
            return menu_option
        return list(recipe_.keys())[menu_option-1]

def add_ingredient_sub_cat(recipe_, main_cat):
    counter = 0
    for key in recipe_[main_cat].keys():
        counter += 1
        print(str(counter) + ". " + key)
    minor_cat_number = u_i_v.user_input_validation_int("Input your desired ingredient (as a number): ", counter)
    if minor_cat_number == "exit":
        return minor_cat_number
    quantity = u_i_v.user_input_validation_is_number("Input your desired quantity (in grams or units): ")
    if quantity == "exit":
        return quantity
    recipe_[main_cat][list(recipe_[main_cat].keys())[int(minor_cat_number)-1]] = int(quantity)
    return recipe_
### add_recipe() end

def edit_recipe(recipes):
### PUT THAT YOU CAN EXIT ANYTIME
     if len(recipes.keys()) > 0: 
        view_exising_recipes(recipes)
        user_in = u_i_v.user_input_validation_int("Which recipe would you like to edit? Please input the corresponding number: ", len(recipes.keys()))
        # convert to integer, check input and adjust show_recipe_ingredients
        if user_in == "exit":
            return user_in
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
            user_in = u_i_v.user_input_validation_int("What would you like to edit:\n1. The recipe name\n2. Add or overwrite recipe ingredients\n3. Delete an ingredient\n 4. Return to the main menu: ", 4)
            if user_in == 1:
                new_recipe_name = input("What should the new name of the recipe be?")
                recipe_ingredients_dict = recipes[recipe_name].copy()
                recipes[new_recipe_name] = recipe_ingredients_dict
                del recipes[recipe_name]
                recipe_name = new_recipe_name
                print(recipes.items())
                return recipes
            elif user_in == 2:
                add_recipe_ingredient_out = add_recipe_ingredients(recipes[recipe_name])
                recipes[recipe_name] = add_recipe_ingredient_out
                return recipes
            elif user_in == 3:
                print("These are the current ingredients:")
                list_of_ingredients = []
                counter = 0
                for key in recipes[recipe_name].keys():
                    for key_internal, value in recipes[recipe_name][key].items():
                        if value > 0:
                            list_of_ingredients.append(key_internal)
                            counter += 1
                            print(str(counter) + ". " + key_internal + " " + str(value))
                while True:
                    user_in = u_i_v.user_input_validation_start_of_word("Which ingredient would you like to delete? Please type the English name of the ingredient: ", list_of_ingredients)
                    key_for_deletion = user_in
                    user_in = u_i_v.user_input_validation_y_n("Is " + key_for_deletion + " the ingredient you want to delete? Answer with 'y' or 'no': ")
                    if user_in == "y":
                        for key in recipes[recipe_name].keys(): #PROBLEM WAS: wrong category key
                            for key_internal, value in recipes[recipe_name][key].items():
                                if key_internal == key_for_deletion:
                                    cat_key_for_deletion = key
                        recipes[recipe_name][cat_key_for_deletion].update({key_for_deletion:0})
                        print(key_for_deletion, " deleted!!!")
                        return recipes
            elif user_in == 4:
                print(recipes.items())
                return recipes
            else:
                print("Unexpected error: 2")
     else:
        print("There are no recipes yet!")

def delete_recipe(recipes):
    view_exising_recipes(recipes)
    user_in = u_i_v.user_input_validation_int("Which recipe would you like to delete? Please input the corresponding number. To return to the main menu, press enter.", len(recipes.keys()))
    if user_in == "":
        return recipes
    else:
        recipes.pop(list(recipes.keys())[user_in-1])
    return recipes
