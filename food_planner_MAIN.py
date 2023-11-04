# -*- coding: utf-8 -*-
import os
import user_input_validation as u_i_v_3
from recipe_functions import *
from edit_food_cat_ingredients import *
from program_setup_load_data_exit_prog import *
from meal_planner import *

def recipe_sub_menu(recipes, ingredients):
    stay_in_sub_menu = True
    while stay_in_sub_menu == True:
        user_in = u_i_v_3.user_input_validation_int("Recipes menu:\nWhat do you wish to do?\n1. View recipe\n2. View recipe ingredients\n3. Add recipe\n4. Edit recipe \n5. Delete recipe\n6. Return to the main menu", 6)
        if user_in == 1:
            print(recipes.keys())
            view_exising_recipes(recipes)
        elif user_in == 2:
            show_recipe_ingredients(recipes)
        elif user_in == 3:
            recipes = add_recipe(recipes, ingredients)
        elif user_in == 4:
            recipes = edit_recipe(recipes)
        elif user_in == 5:
            recipes = delete_recipe(recipes)
        elif user_in == 6:
            return [recipes, ingredients]

def category_ingredients_sub_menu(recipes, ingredients):
    stay_in_sub_menu = True
    print("These are the current food categories and their ingredients:")
    view_categories_and_ingredient(ingredients)
    while stay_in_sub_menu == True:
        user_in = u_i_v_3.user_input_validation_int("What do you wish to do?\n1. Add, rename or delete food categories\n2. Add, change category of, rename and delete ingredients\n3. Return to the main menu", 3)
#        user_in = u_i_v_3.user_input_validation_int("Ingredients menu:\nWhat do you wish to do?\n1. Add new ingredient\n2. Edit ingredient\n3. Delete ingredient\n4. Return to the main menu", 4)
        if user_in == 1:
            user_in = u_i_v_3.user_input_validation_int("What do you wish to do?\n1. View categories and ingredients again\n2. Add a food category\n3. Rename food category\n4. Delete food category\n5. Exit", 5)
            if user_in == 1:
                view_categories_and_ingredient(ingredients)
            elif user_in == 2:
                recipes, ingredients = add_new_food_cat(recipes, ingredients)
            elif user_in == 3:
                recipes, ingredients = rename_food_cat(recipes, ingredients) 
            elif user_in == 4:
                ingredients = delete_food_cat(recipes, ingredients)
            elif user_in == 5:
                return [recipes, ingredients]
        elif user_in == 2:
            user_in = u_i_v_3.user_input_validation_int("What do you wish to do?\n1. View categories and ingredients again\n2. Add new ingredients? \n3. Rename ingredients\n4. Delete ingredients\n5. Exit", 5)
            if user_in == 1:
                view_categories_and_ingredient(ingredients)
            elif user_in == 2:
                recipes, ingredients = add_new_ingredient(recipes, ingredients)
            elif user_in == 3:
                ingredients = rename_ingredient(ingredients)
            elif user_in == 4:
                ingredients = delete_ingredient(ingredients)
            elif user_in == 5:
                return [recipes, ingredients]
        elif user_in == 3:
            return [recipes, ingredients]
#change_ingredient_category(recipes, ingredients)
#view_ingredients_only(ingredients)
#view_categories_and_ingredient(ingredients)
#view_food_cat(ingredients)


def meal_panner_sub_menu(meal_planner, meal_plans_saved, recipes, ingredients, reg_shopping_list, user_pref):
    stay_in_sub_menu = True
    while stay_in_sub_menu == True:
        user_in = u_i_v_3.user_input_validation_int("Meal planner menu:\nWhat do you wish to do?\n1. Plan new meals and generate shopping list\n2. Create list of additional shopping list items\n3. Return to the main menu", 3)
        if user_in == 1:    
            meal_planner, meal_plans_saved = create_meal_plan(meal_planner, meal_plans_saved, recipes, user_pref)
        if user_in == 2:    
            reg_shopping_list = create_edit_reg_shopping_list(reg_shopping_list)
        elif user_in == 3:
            return [meal_planner, meal_plans_saved, reg_shopping_list]

def main_menu(default_wd, meal_plans, recipes, ingredients,  meal_planner, meal_plans_saved, reg_shopping_list, user_pref):
    print("Welcome to your Food Planner program!")
    stay_in_program = True
    while stay_in_program == True:
        user_in = u_i_v_3.user_input_validation_int("Main menu:\n1. Recipes: view, add, edit, delete, see ingredients \n2. Food categories: view, add, edit, delete\n3. Ingredients: add, edit, delete\n4. Food plan and shopping list\n5. Preferences\n6.Exit program\n", 6)
        if user_in == 1:
            try:  
                recipes, ingredients = recipe_sub_menu(recipes, ingredients) 
            except Exception as e: 
                print(e)
        elif user_in == 2:
            try:  
                recipes, ingredients = category_ingredients_sub_menu(recipes, ingredients) 
            except Exception as e: 
                print(e)
        elif user_in == 3:
            meal_planner, meal_plans_saved, reg_shopping_list = meal_panner_sub_menu(meal_planner, meal_plans_saved, recipes, ingredients, reg_shopping_list, user_pref)
        elif user_in == 4:
            try:  
                user_pref = set_meal_planner_preferences(user_pref)
            except Exception as e: 
                print(e)
        elif user_in == 5:
            try:  
                stay_in_program = exit_program(default_wd, meal_plans, recipes, ingredients, meal_planner, meal_plans_saved, reg_shopping_list, user_pref)
            except Exception as e: 
                print(e)
        else:
            print("Unexpected error: 1")

def run_program():
    program_setup()
    default_wd, meals, recipes, ingredients, meal_planner, meal_plans_saved, reg_shopping_list, user_pref = load_data()
    check_meal_planner_year(meal_planner)
    main_menu(default_wd, meals, recipes, ingredients, meal_planner, meal_plans_saved, reg_shopping_list, user_pref)

run_program()




