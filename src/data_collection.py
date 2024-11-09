import requests
import pandas as pd
import os
from config.config import API_ID, API_KEY, BASE_URL
from omnivore_menu import omnivore_menu
from vegetarian_menu import vegetarian_menu
from fast_food_menu import fast_food_menu

# Define nutrients to extract and their corresponding attr_id
NUTRIENTS_ATTR_IDS = {
    "Calories": "nf_calories",
    "Protein": "nf_protein",
    "Fat": "nf_total_fat",
    "Saturated Fat": 606,
    "Monounsaturated Fat": 645,
    "Polyunsaturated Fat": 646,
    "Carbohydrates": "nf_total_carbohydrate",
    "Fiber": "nf_dietary_fiber",
    "Sugars": "nf_sugars",
    "Calcium": 301,
    "Iron": 303,
    "Magnesium": 304,
    "Phosphorus": 305,
    "Potassium": 306,
    "Sodium": "nf_sodium",
    "Zinc": 309,
    "Copper": 312,
    "Manganese": 315,
    "Selenium": 317,
    "Vitamin A": 318,
    "Vitamin C": 401,
    "Vitamin D": 324,
    "Vitamin E": 323,
    "Vitamin K": 430,
    "Thiamin": 404,
    "Riboflavin": 405,
    "Niacin": 406,
    "Vitamin B6": 415,
    "Folate": 417,
    "Vitamin B12": 418,
    "Pantothenic Acid": 410,
    "Choline": 421,
    "Omega-3 Fatty Acids": 851,
    "Omega-6 Fatty Acids": 852,
    "Cholesterol": "nf_cholesterol"
}

# Define menus to process
menus = {
    "Omnivore": omnivore_menu,
    "Vegetarian": vegetarian_menu,
    "Fast Food": fast_food_menu
}

# Function to fetch nutrient data for a single ingredient
def fetch_nutrition_data(ingredient):
    headers = {
        "x-app-id": API_ID,
        "x-app-key": API_KEY,
    }
    
    response = requests.post(
        f"{BASE_URL}natural/nutrients",
        headers=headers,
        json={"query": ingredient}
    )
    
    if response.status_code == 200:
        data = response.json()
        nutrition_info = data['foods'][0]
        
        # Extract relevant nutrient values
        nutrient_data = {"Ingredient": ingredient}
        for nutrient, attr_id in NUTRIENTS_ATTR_IDS.items():
            if isinstance(attr_id, str):  # Direct field
                nutrient_data[nutrient] = nutrition_info.get(attr_id, "N/A")
            else:  # Look up in full_nutrients
                value = next((item['value'] for item in nutrition_info['full_nutrients'] if item['attr_id'] == attr_id), "N/A")
                nutrient_data[nutrient] = value
        return nutrient_data
    else:
        print(f"Failed to fetch data for {ingredient}")
        print("Status Code:", response.status_code)
        print("Response:", response.text)
        return None

# Collect data for all days in each menu
data_rows = []
for menu_type, days in menus.items():
    print(f"Processing menu type: {menu_type}")
    for day, meals in days.items():
        print(f"  Fetching data for {day}...")
        for meal, ingredients in meals.items():
            print(f"    Meal: {meal}")
            for ingredient in ingredients:
                nutrient_data = fetch_nutrition_data(ingredient)
                if nutrient_data:
                    nutrient_data["Menu Type"] = menu_type  # Add menu type for context
                    nutrient_data["Day"] = day  # Add day for context
                    nutrient_data["Meal"] = meal  # Add meal name for context
                    data_rows.append(nutrient_data)

# Create a DataFrame from the collected data
df = pd.DataFrame(data_rows)

# Save the data to a CSV file for EDA
output_dir = os.path.join("data", "raw")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "7_days_multi_menu_nutrition_data.csv")
df.to_csv(output_path, index=False)
print(f"Data successfully saved to '{output_path}'")











