import pickle
import os
import meal_planner as m_p

def program_setup():
    file_not_loading = True
    while file_not_loading == True:
        try:
            with open('savedRecipes.pkl', 'rb') as file:
                default_wd, meal_plans, recipes, ingredients, meal_planner, meal_plans_saved, reg_shopping_list, user_pref = pickle.load(file)
            file_not_loading = False
        except:
            print("Your Food Planner data has not run in this directory yet:\n" + os.getcwd() +"\nPerforming first time setup...") 
            default_wd = ""
            meal_plans = {} # Think this is redundant
            meal_plans_saved = {}
            user_pref = {"n_of_eaters":"", "plan_breakfast":""}
            recipes = {} 
            reg_shopping_list = {}
            ingredients = {
            "Proteins": {
                "Beef (Carne de res)": 0,
                "Pork (Cerdo)": 0,
                "Poultry (Aves de corral)": 0,
                "Lamb (Cordero)": 0,
                "Seafood (Mariscos)": 0,
                "Eggs (Huevos)": 0
            },
            "Dairy and Dairy Alternatives": {
                "Milk (Leche)": 0,
                "Cheese (Queso)": 0,
                "Butter (Mantequilla)": 0,
                "Yogurt (Yogur)": 0,
                "Cream (Crema)": 0,
                "Non-Dairy Alternatives (Alternativas lácteas sin lácteos)": 0
            },
            "Grains and Starches": {
                "Pasta (Pasta)": 0,
                "Rice (Arroz)": 0,
                "Bread (Pan)": 0,
                "Potatoes (Papas)": 0,
                "Quinoa (Quinua)": 0,
                "Polenta (Polenta)": 0
            },
            "Herbs and Spices": {
                "Basil (Albahaca)": 0,
                "Rosemary (Romero)": 0,
                "Thyme (Tomillo)": 0,
                "Oregano (Orégano)": 0,
                "Cinnamon (Canela)": 0,
                "Paprika (Pimentón)": 0,
                "Black Pepper (Pimienta negra)": 0,
                "Salt (Sal)": 0,
                "Nutmeg (Nuez moscada)": 0,
                "Coriander (Cilantro)": 0,
                "Cumin (Comino)": 0
            },
            "Fats and Oils": {
                "Olive Oil (Aceite de oliva)": 0,
                "Vegetable Oil (Aceite vegetal)": 0,
                "Coconut Oil (Aceite de coco)": 0,
                "Avocado Oil (Aceite de aguacate)": 0,
                "Lard (Manteca)": 0,
                "Shortening (Manteca vegetal)": 0
            },
            "Sweeteners": {
                "Sugar (Azúcar)": 0,
                "Honey (Miel)": 0,
                "Maple Syrup (Jarabe de arce)": 0,
                "Agave Nectar (Néctar de agave)": 0
            },
            "Condiments and Sauces": {
                "Ketchup": 0,
                "Mustard (Mostaza)": 0,
                "Mayonnaise (Mayonesa)": 0,
                "BBQ Sauce (Salsa barbacoa)": 0,
                "Salad Dressings (Aderezos para ensaladas)": 0,
                "Tomato Sauce (Salsa de tomate)": 0,
                "Gravy (Salsa de carne)": 0
            },
            "Nuts and Seeds": {
                "Almonds (Almendras)": 0,
                "Walnuts (Nueces)": 0,
                "Pecans (Nueces pecanas)": 0,
                "Hazelnuts (Avellanas)": 0,
                "Cashews (Anacardos)": 0,
                "Macadamia Nuts (Nueces de macadamia)": 0,
                "Pistachios (Pistachos)": 0,
                "Pine Nuts (Piñones)": 0,
                "Brazil Nuts (Nueces de Brasil)": 0,
                "Sunflower Seeds (Semillas de girasol)": 0,
                "Pumpkin Seeds (Semillas de calabaza)": 0,
                "Chia Seeds (Semillas de chía)": 0,
                "Flaxseeds (Semillas de lino)": 0,
                "Sesame Seeds (Semillas de sésamo)": 0
            },
            "Vegetables": {
                "Spinach (Espinaca)": 0,
                "Lettuce (Lechuga)": 0,
                "Kale (Col rizada)": 0,
                "Broccoli (Brócoli)": 0,
                "Cauliflower (Coliflor)": 0,
                "Brussels sprouts (Coles de Bruselas)": 0,
                "Carrots (Zanahorias)": 0,
                "Potatoes (Papas)": 0,
                "Beets (Remolachas)": 0,
                "Tomatoes (Tomates)": 0,
                "Bell Peppers (Pimientos morrones)": 0,
                "Eggplants (Berenjenas)": 0,
                "Onions (Cebollas)": 0,
                "Garlic (Ajo)": 0,
                "Shallots (Chalotes)": 0,
                "Beans (Frijoles)": 0,
                "Lentils (Lentejas)": 0,
                "Peas (Guisantes)": 0
            },
            "Fruits": {
                "Apples (Manzanas)": 0,
                "Strawberries (Fresas)": 0,
                "Blueberries (Arándanos)": 0,
                "Oranges (Naranjas)": 0,
                "Lemons (Limones)": 0,
                "Limes (Limones verdes)": 0,
                "Peaches (Duraznos)": 0,
                "Plums (Ciruelas)": 0,
                "Cherries (Cerezas)": 0,
                "Bananas (Plátanos)": 0,
                "Watermelon (Sandía)": 0,
                "Cantaloupe (Melón cantalupo)": 0
            }
        }
            meal_planner = m_p.create_meal_calendar()
            user_pref = m_p.set_meal_planner_preferences(user_pref)
            with open('savedRecipes.pkl', 'wb') as file:
                pickle.dump([default_wd, meal_plans, recipes, ingredients, meal_planner, meal_plans_saved, reg_shopping_list, user_pref], file)
            file_not_loading = False
            print("Done!")

def load_data():
    with open(r"savedRecipes.pkl", "rb") as file:
        default_wd, meal_plans, recipes, ingredients, meal_planner, meal_plans_saved, reg_shopping_list, user_pref = pickle.load(file)
        return [default_wd, meal_plans, recipes, ingredients, meal_planner, meal_plans_saved, reg_shopping_list, user_pref]
    
def exit_program(default_wd, meal_plans, recipes, ingredients, meal_planner, meal_plans_saved, reg_shopping_list, user_pref):
    print("Saving changes...")
    with open('savedRecipes.pkl', 'wb') as file:
        pickle.dump([default_wd, meal_plans, recipes, ingredients, meal_planner, meal_plans_saved, reg_shopping_list, user_pref], file)
    print("Thank you for visiting!")
    stay_in_program = False
    return stay_in_program