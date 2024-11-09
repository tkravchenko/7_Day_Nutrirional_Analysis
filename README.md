# 7-Day Nutritional Analysis of Healthy Omnivore, Fast Food, and Vegetarian Diets

## Project Overview
This project aims to analyze and compare the nutritional quality, caloric intake, and ingredient quality across three different diets over a week: healthy omnivore, fast food, and vegetarian. The focus is on retrieving nutrient information, assessing nutrient quality indicators (such as fiber and refined sugars), and visualizing findings to highlight the differences among these diets.

## Objective
The objective of this project is to provide insights into the dietary habits represented by these menus and to recommend healthier choices based on nutritional analysis.

## Technologies and Libraries
- **Data Retrieval**:
  - **Nutritionix API**: the primary source for nutritional data and ingredient quality indicators.
  - **Python (requests)**: used for making API calls to fetch data.
  
- **Data Processing**:
  - **Python (pandas)**: for data cleaning, manipulation, aggregation, and calculations.
  
- **Data Visualization**:
  - **Power BI**: to create an interactive dashboard showcasing nutrient comparisons, health insights, and quality indicators.
  - **Matplotlib/Seaborn**:fFor initial visualizations or exploratory data analysis within the Python environment.

## Project Steps
1. **Meal Plan Definition and API Setup**
   - Define a 7-day meal plan for each diet using recipes from [Spoon](https://spoon.com.ua/en) for the omnivore and vegetarian menus, and popular fast food items for the fast food menu.
   - Set up the Nutritionix API for data retrieval.

2. **Data Collection**
   - Retrieve nutritional data for each food item in the meal plans, including macronutrients and micronutrients.
   - Clean and format the data using pandas.

3. **Data Cleaning**
   - Missing Values: identified and handled missing values, either by imputing with averages or removing entries with excessive missing data.
   - Standardization: ensured consistent units across the dataset, converting macronutrients to grams and micronutrients to milligrams.
   - Formatting: organized the dataset into a structured format (pandas DataFrame) for efficient analysis.
   - Outlier Detection: applied statistical methods to identify and address outliers in calorie and nutrient content.

4. **Exploratory Data Analysis (EDA)**
   - Aggregate daily nutrient totals and averages for each diet.
   - Calculate quality indicators for fiber, refined sugars, and artificial ingredients.
   - Visualize nutrient distribution across diets and perform correlation analysis.

5. **Data Visualization in Power BI**
   - Create a dashboard displaying comparisons of macronutrients, micronutrients, and health risk indicators.

6. **Insights and Recommendations**
   - Summarize dietary insights and provide health recommendations based on the analysis.

## Results and Findings
- The vegetarian diet demonstrated the highest nutritional quality, with beneficial levels of fiber and lower cholesterol compared to the other diets.
- The fast food diet was characterized by high calories, saturated fat, and sodium, indicating a need for healthier alternatives.
- Recommendations include incorporating more vegetables, whole grains, and lean proteins in the fast food diet and considering plant-based options in the omnivore diet.

## Conclusion
This analysis highlights the differences in nutritional quality among various diets and underscores the importance of making informed dietary choices for better health outcomes.

## Requirements
Ensure you have the following libraries installed to run the project:
- pandas
- numpy
- requests
- matplotlib
- seaborn

## Acknowledgements
Special thanks to the Nutritionix API for providing nutritional data and Spoon for recipe inspiration.


