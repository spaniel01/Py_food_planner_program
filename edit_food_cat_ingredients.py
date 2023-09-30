import user_input_validation as u_i_v_2

### View functions
def view_categories_and_ingredient(ingredients):
    print("These are the current food categories and their ingredients: ")
    counter = 0
    for food_cat in ingredients.keys():
        list_of_ingredients = []
        counter += 1
        for food_ingredient in ingredients[food_cat].keys():
            list_of_ingredients.append(food_ingredient)
        list_of_ingredients.sort()
        print(counter, food_cat, ": " , ", ".join(list_of_ingredients), "\n")
    return counter

def view_food_cat(ingredients):
    counter = 0
    for cat in ingredients.keys():
        counter += 1
        print(str(counter) + ". " + cat)
    return counter

def view_ingredients_only(ingredients):
    print("This is a list of all ingredients: ")
    list_of_ingredients = []
    for outer_key in ingredients.keys():
        for inner_key in ingredients[outer_key].keys():
            list_of_ingredients.append(inner_key)
    list_of_ingredients.sort()
    print(", ".join(list_of_ingredients))


def view_ingredients_only_list(ingredients):
    print("This is a list of all ingredients: ")
    list_of_ingredients = []
    for outer_key in ingredients.keys():
        for inner_key in ingredients[outer_key].keys():
            list_of_ingredients.append(inner_key)
            list_of_ingredients.sort()
    counter = 0
    for entry in list_of_ingredients:
            counter += 1
            print(counter, ".", entry)
    return [counter, list_of_ingredients]


### Changing values: categories
def add_new_food_cat(recipes, ingredients):
    view_categories_and_ingredient(ingredients)
    run_once = -1
    while True:
        run_once += 1
        if run_once < 1:
            user_in_food_cat = input("Which food category would you like to add? Type exit to leave/ cancel")
        else:
            user_in_food_cat = input("Would you like to add another food category? Type exit to leave/ cancel")
        if user_in_food_cat == "exit":
            return [recipes, ingredients]
        ingredients[user_in_food_cat] = {}
        out = u_i_v_2.user_input_validation_y_n("Would you like to add new ingredients to this category now? Answer with y or n, type exit to cancel: ")
        if out == "exit":
            return [recipes, ingredients]
        elif out == "n":    
            #Update recipes
            for recipe_ in recipes.keys():
                recipes[recipe_][user_in_food_cat] = {}
        elif out == "y":
            while True:
                user_in_food_ingredient = input("Which ingredient would you like to add? Type exit to cancel: ")
                if user_in_food_ingredient == "exit":
                    break
                ingredients[user_in_food_cat][user_in_food_ingredient] = 0
                # Update recipe
                for recipe_ in recipes.keys():
                    recipes[recipe_][user_in_food_cat][user_in_food_ingredient] = 0


def rename_food_cat(recipes, ingredients):
    counter = view_categories_and_ingredient(ingredients)
    run_once = -1
    while True:
        run_once += 1
        if run_once < 1:
            old_category = u_i_v_2.user_input_validation_int("Which food category would you like to edit? ", counter) 
        else:
            old_category = u_i_v_2.user_input_validation_int("Which other food category would you like to edit? ", counter)
        if old_category == "exit":
            return [recipes, ingredients]
        print("This food category includes the following ingredients:\n")
        counter = 0 
        for ingredient in ingredients[list(ingredients.keys())[old_category-1]]:
            counter += 1
            print(str(counter) + ". " + ingredient)
        new_category_name = input("If you want to return to the main menu, type exit. \nWhat should the new name of the food category be?")
        if new_category_name == "exit":
            return [recipes, ingredients]
        if len(ingredients[list(ingredients.keys())[old_category-1]].items()) > 0:
            old_category_ingredients = ingredients[list(ingredients.keys())[old_category-1]]
            del ingredients[list(ingredients.keys())[old_category-1]]
            ingredients[new_category_name] = old_category_ingredients
            # Update recipes
            for recipe_ in recipes.keys():
                old_category_ingredients = recipes[recipe_][old_category]
                del recipes[recipe_][old_category]
                recipes[recipe_][new_category_name] = old_category_ingredients
        else:
            del ingredients[list(ingredients.keys())[old_category-1]]
            ingredients[new_category_name] = {}
            #Update recipes
            for recipe_ in recipes.keys():
                del recipes[recipe_][list(ingredients.keys())[old_category-1]]
                recipes[recipe_][new_category_name] = {}


def delete_food_cat(recipes, ingredients):
    while True:
        print("You are about to delete a food category.\nType 'exit' to return to the main menu.\nThese are the current food categories: ")
        counter = view_food_cat(ingredients)
        category_to_delete = u_i_v_2.user_input_validation_int("Which food category would you like to delete? ", counter)
        if category_to_delete == "exit":
            return [recipes, ingredients]
        print("This food category includes the following ingredients:\n")
        counter = 0 
        for ingredient in ingredients[list(ingredients.keys())[category_to_delete-1]]:
            counter += 1
            print(str(counter) + ". " + ingredient)
        print("These ingredients are used in the following recipes:")
        counter = 0
        for recipe_ in recipes.keys():
            if recipes[recipe_].keys() == list(ingredients.keys())[category_to_delete-1]:
                for ingredient_, value in recipes[recipe_][list(ingredients.keys())[category_to_delete-1]].items(): ########################## SEE ingredient_
                    if value > 0:
                        counter += 1
                        print(counter, " ", recipe_)
        user_in_y_n = u_i_v_2.user_input_validation_y_n("Are you sure you want to delete this category? This does not affect existing recipes. Answer with 'y' or 'n': ")
        if user_in_y_n == "exit":
            return [recipes, ingredients]
        if user_in_y_n == "y":
            del ingredients[list(ingredients.keys())[category_to_delete-1]]
        elif  user_in_y_n == "n":
            continue
        else:
            print("Invalid user input. Please try again!")
        
### Changing values: ingredients
def add_new_ingredient(recipes, ingredients):
    while True:
        print("You are about to add a new ingredient.\nType 'exit' to return to the main menu.\nThese are the current ingredients: ")
        counter = view_categories_and_ingredient(ingredients)
        user_in_category = u_i_v_2.user_input_validation_int("Which category does the ingredient belong to? ", counter)
        if user_in_category == "exit":
            return [recipes, ingredients]
        user_in_ingredient = input("What is the new ingredient called? ")
        if user_in_ingredient == "exit":
            return [recipes, ingredients]
        ingredients[list(ingredients.keys())[user_in_category-1]][user_in_ingredient] = 0
        # Update recipes
        for recipe_ in recipes.keys():
            for category_ in recipes[recipe_]:
                recipes[recipe_][category_][user_in_ingredient] = 0
        return [recipes, ingredients]

def rename_ingredient(ingredients, recipes):
    print("You are about to edit an ingredient.\nType 'exit' to return to the main menu.\nThese are the current ingredients: ")
    list_of_ingredients = []
    for outer_key in ingredients.keys():
        for inner_key in ingredients[outer_key].keys():
            list_of_ingredients.append(inner_key)
    list_of_ingredients_print = list_of_ingredients.copy()       
    list_of_ingredients_print.sort()
    print(", ".join(list_of_ingredients_print))
    selected_ingredient = u_i_v_2.user_input_validation_start_of_word("Which ingredient do you want to edit? Please type its English name: ", list_of_ingredients)
    if selected_ingredient == "exit":
         return ingredients
    ingredient_edited = input("What is the new name of the ingredient? ")
    if ingredient_edited == "exit":
         return ingredients
    for outer_key in ingredients.keys():
        if selected_ingredient in ingredients[outer_key].keys():
            break
    del ingredients[outer_key][selected_ingredient]
    ingredients[outer_key][ingredient_edited] = 0
    # Update recipes
    for recipe_ in recipes.keys():
        for category in recipes[recipe_].keys():
            if selected_ingredient in recipes[recipe_][category].keys():
                ingredient_quantity = recipes[recipe_][category][selected_ingredient]
                del recipes[recipe_][category][selected_ingredient]
                recipes[recipe_][category][ingredient_edited] = ingredient_quantity
    return [recipes, ingredients]

def change_ingredient_category(ingredients, recipes):
    counter, list_of_ingredients = view_ingredients_only_list(ingredients)
    ingred_i = u_i_v_2.user_input_validation_int("Which ingredient do you want to move? ", counter)
    if ingred_i == "exit":
        return [ingredients, recipes]
    counter = view_food_cat(ingredients)
    new_category = u_i_v_2.user_input_validation_int("Which category do you want to move the ingredient to? ", counter)
    if new_category == "exit":
        return [ingredients, recipes]
    ingredients[new_category][list_of_ingredients[ingred_i-1]] = 0
    for food_cat in ingredients.keys():
        for food_ingred in ingredients[food_cat]:
            if food_ingred == list_of_ingredients[ingred_i-1]:
                ingred_to_delete_from = food_cat
    del ingredients[ingred_to_delete_from][list_of_ingredients[ingred_i-1]]
    # Update all recipes
    for recipe_ in recipes:
            previous_ingred_value = recipes[recipe_][ingred_to_delete_from][list_of_ingredients[ingred_i-1]]
            del recipes[recipe_][ingred_to_delete_from][list_of_ingredients[ingred_i-1]]
            recipes[recipe_][new_category][list_of_ingredients[ingred_i-1]] = previous_ingred_value
    return [ingredients, recipes]


def delete_ingredient(ingredients):
    print("Here you can edit an ingredient, that is, change its name, but not its category.\nIf you want to edit an ingredient's category, simply delete the ingredient and then add a new ingredient.\nType 'exit' to return to the main menu.\nThese are the current ingredients: ")
    list_of_ingredients = []
    counter = 0
    for outer_key in ingredients.keys():
        for inner_key in ingredients[outer_key].keys():
            counter += 1
            print(counter, " ", inner_key)
            list_of_ingredients.append(inner_key)
    ingredient_to_delete = u_i_v_2.user_input_validation_start_of_word("Which ingredient do you want to delete? Please type its English name: ", list_of_ingredients)
    if ingredient_to_delete == "exit":
         return ingredients
    for outer_key in ingredients.keys():
            for inner_key in ingredients[outer_key].keys():
                if inner_key == ingredient_to_delete:
                    del ingredients[outer_key][inner_key]
    return ingredients
