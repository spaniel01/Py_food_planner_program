import datetime 
import copy
import calendar
from datetime import date
from datetime import datetime
from datetime import timedelta
import pandas as pd
import numpy as np
import user_input_validation as u_i_v_3

def create_meal_calendar(): #year_ integer, string first_weekday_of_January
    print("You need to set up the food calendar for the year ", str(date.today().year), ".")
    first_weekday_of_January = input("Please enter the name of the first day of January this year, for example, 'Monday': ")
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    while True:
        if first_weekday_of_January in weekdays:
            break
        else:
            print("Invalid input. Please provide a weekday name.")
    year_ = date.today().year
    year = []
    year += [year_]*365*3

    months = {"January":31, "February":28, "March":31, "April":30, "May":31, "June":30, "July":31, "August":31, "September":30, "October":31, "November":30, "December":31}
    month_replications = []
    for month, number_of_days in months.items():
        counter_day = 0
        while counter_day < number_of_days*3: 
            counter_day += 1
            month_replications.append(month)

    month = []
    month_counter = 0
    for number_of_days in months.values():
        month_counter += 1
        month += [month_counter]*number_of_days*3

    ### Last day number of first calendar week
    end_of_first_week_num = 0
    for weekday in weekdays:
        end_of_first_week_num += 1
        if weekday == first_weekday_of_January:
            break

    calendar_weeks = []
    calendar_week = 1
    days_a_year = 365
    calendar_weeks += [1]*end_of_first_week_num*3
    counter_days_a_year = end_of_first_week_num 
    counter_calendar_week = 1
    while counter_days_a_year + 7 < days_a_year:
        counter_days_a_year += 7
        calendar_week += 1
        calendar_weeks += [calendar_week]*7*3
    num_days_last_week_of_year = days_a_year - counter_days_a_year 
    calendar_week += 1
    calendar_weeks += [calendar_week]*num_days_last_week_of_year*3

    weekdays_list = []
    first_weekday_of_January
    counter = 0
    for weekday_ in weekdays:
        counter += 1
        if weekday_ == first_weekday_of_January:
            weekdays_list += weekdays[counter-1:]
    for i in range(0, 51):
        weekdays_list += weekdays
    weekdays_list += weekdays[:(365-len(weekdays_list))]
    weekdays_list = [val for val in weekdays_list for _ in (0, 1, 2)]

    days = []
    for max_number_of_days in months.values():
        month_range = range(1, max_number_of_days+1)
        for day_number in month_range:
            days += [day_number]*3

    meals = ["breakfast", "lunch", "supper"]*365
    meal_planner = pd.DataFrame(zip(year, month_replications, month, calendar_weeks, days, weekdays_list, meals), columns = ["year", "month_name", "month", "calendar_week", "day", "weekday", "meal"])
    meal_planner["date"] = pd.to_datetime(meal_planner[['year', 'month', 'day']])
#    meal_planner.set_index("date", inplace = True)
    meal_planner["recipe"] = ""
    return meal_planner

def check_meal_planner_year(meal_planner):
    if len(meal_planner[meal_planner["year"] == int(date.today().year)]) == 365*3:
        return meal_planner
    else:
        meal_planner_new = create_meal_calendar()
        meal_planner = pd.concat([meal_planner, meal_planner_new])
        meal_planner.reset_index(inplace=True)
        return meal_planner

def set_meal_planner_preferences(user_pref):
    print("To make the use of the meal planner more convenient, please enter information about your preferences.")
    user_pref_n_of_eaters = u_i_v_3.user_input_validation_is_number("How many people do you usually want to prepare a meal for?")
    if user_pref_n_of_eaters == "exit":
        return user_pref
    user_pref_plan_breakfast = u_i_v_3.user_input_validation_y_n("Do you wish to plan for breakfast from Monday to Friday? Please answer with 'y' and 'n'.")
    if user_pref_plan_breakfast == "exit":
        return user_pref
    if user_pref_plan_breakfast == "y":
        user_pref_plan_breakfast = True
    else:
        user_pref_plan_breakfast = False
    user_pref["n_of_eaters"] = user_pref_n_of_eaters
    user_pref["plan_breakfast"] = user_pref_plan_breakfast
    return user_pref

def meal_planner_date_input(message):
    while True:
        date = input(message)
        print(date)
        if date == "exit":
            print("wtf")
            return date
        try:
            date = datetime.strptime(date, "%Y-%m-%d")
            return date
        except:
            print("Format not correct, please try again.")

### THIS REQUIES BOTH MEAL_PLANNER AND RECIPES objects, which may cause problems when loading scripts (check how you did it with the other ones)
def create_meal_plan(meal_planner, meal_plans_saved, recipes, user_pref):
    print("You can now plan your meals for the coming days.")
    user_in = u_i_v_3.user_input_validation_y_n("Do you want to plan for the next 7 days, starting with today's dinner?\n Please answer with 'y' for yes or 'n' for no: ")
    if user_in == "n":
        start_date = meal_planner_date_input("Enter the start date. Please use the 'yyyy-mm-dd' format: ")
        end_date = meal_planner_date_input("Enter the end date. Please use the 'yyyy-mm-dd' format: ")
    else:
        start_date = date.today().strftime("%Y-%m-%d")
        end_date = datetime.strptime(start_date,"%Y-%m-%d") + timedelta(days=7)
        end_date = end_date.strftime("%Y-%m-%d")
    meal_planner_temp = meal_planner[(meal_planner["date"] >= pd.to_datetime(start_date)) & (meal_planner["date"] <= pd.to_datetime(end_date))].copy()
    if user_pref["plan_breakfast"] == False:
        meal_planner_temp = meal_planner_temp[meal_planner_temp["meal"] != "breakfast"].copy()
    for a, b in meal_planner_temp.iterrows():
        print(a)
        print("On", b.weekday, b.date.strftime("%Y-%m-%d"), "what would you like to eat for", str(b.meal), "?")
        counter = 0
        for meal_ in recipes.keys():
            counter += 1
            print(counter, ".", meal_)
        user_in_meal = u_i_v_3.user_input_validation_int("Please input a meal number:", counter)
        meal_planner_temp.at[a,"recipe"] = list(recipes.keys())[user_in_meal-1]
    print("This is your meal plan:")
    for i_, meal_series in meal_planner_temp.iterrows():
        print(meal_series.date.strftime("%Y-%m-%d"), meal_series.weekday, ":", meal_series.recipe)
    print("Do you wish to edit the meal plan?") #################################################################### Insert edit func
    user_in = u_i_v_3.user_input_validation_y_n("Do you want to save this meal plan for future referenc?")
    if user_in == "y":
        user_in = input("What would you like to call the meal plan?")
        meal_plans_saved[user_in] = meal_planner_temp
        meal_planner.columns
        meal_planner = pd.concat([meal_planner, meal_planner_temp]).drop_duplicates(["date", "meal"], keep='last')
        meal_planner.columns
        meal_planner.sort_values(["date", "meal"], ascending = True, inplace = True)
    else:
        print(meal_planner)
        print(meal_planner.columns)
        meal_planner = pd.concat([meal_planner, meal_planner_temp]).drop_duplicates(["date", "meal"], keep='last')
        print(meal_planner.columns)
        meal_planner.sort_values(["date", "meal"], ascending= True, inplace = True)
    user_in = u_i_v_3.user_input_validation_y_n("Do you want to generate the shopping list now?")
    if user_in == "y":
        shopping_list_meals = list(meal_planner_temp.recipe)
        shopping_list = {}
        for recipe in shopping_list_meals:
            for key in recipes[recipe].keys():
                    for key_internal, value in recipes[recipe][key].items():
                        if value > 0 and key_internal not in shopping_list:
                            shopping_list[key_internal] = value * user_pref["n_of_eaters"]
                        elif value > 0:
                            exisiting_value = shopping_list[key_internal]
                            shopping_list[key_internal] = exisiting_value + value * user_pref["n_of_eaters"]
                        else:
                            continue
        file_name = str(date.today().strftime("%Y-%m-%d")) + "_shopping_list.txt"
        with open(file_name, 'w', encoding="utf-8") as f: 
            f.write("Shopping list:\n-------------")
            for key, value in shopping_list.items(): 
                f.write('%s:%s\n' % (key, value))
    return [meal_planner, meal_plans_saved]
        
def edit_meal_plan(meal_planner, meal_plans_saved, user_pref, recipes, meal_plan_just_created = False):
    if meal_plan_just_created == True:
        pass
    else:
        print("These are the current meal plans:\n")
        for meal_plan_ in meal_plans_saved.keys():
            counter =+ 1
            print(counter, ".", meal_plan_)
        user_in = u_i_v_3.user_input_validation_int("Please input a meal plan number:", counter)
        ### Make option here to see what they want to edit: rename meal plan or actual meal plan 
        meal_planner_temp = meal_plans_saved[list(meal_plans_saved.keys())[user_in-1]].copy()
        print("This is the selected meal plan:\n")
        counter_meal = 0
        counter_day = 1
        max_meals = meal_planner_temp.groupby(date).count().unique()  ### better, take unique dates, make list, iterate through, filtering df_temp by date, doing count and depending on count indicating day
        for row in range(0, len(meal_planner_temp)):
            if counter_meal == max_meals:
                counter_meal = 0
                counter_day += 1
            print("Day ", counter_day, meal_planner_temp[row].meal, meal_planner_temp[row].meal.recipe)
#        day = u_i_v_3.user_input_validation_int("Which day do you want to edit?", XXX) # make XXX n of unique dates
#        meal = u_i_v_3.user_input_validation_word("Which meal do you want to edit?", list_of_words) # make list_of_words by filtering by date
        # use day and meal to overwrite value with new meal

# Rename meal plan
# Delete meal plan
# Change defaults for meal planner



    #### Would u like to make any changes? y_n input validation
    #### Please enter date and meal for which you want to make changes
    #### Would you like to change the number of persons to cook for from the default?
    #### Would you like to save this meal plan to use in the future? locals() to give it 
    #### print(calculating shopping list)

### View meal plans with option to select them for a given week, allow editing of meal plans. These are just dfs with column for day (1-7), meal and recipe, day overwritten by day in meal planner, meal and recipe inserted in meal planner
