# Task 1: The Dynamic Currency Converter with Added Value

""" Requirements 
1. Starting Value: Prompt the user to enter an amount in Euros (EUR). Store this value in a suitable float variable.
2. Exchange Rates: Define two different exchange rates as float variables directly in your code:
   A rate from EUR to US Dollar (USD), e.g., 1 EUR = 1.08 USD.
   A rate from EUR to Japanese Yen (JPY), e.g., 1 EUR = 165.25 JPY.
3. USD Calculation: Calculate how many USD the entered Euro amount corresponds to. Store the result in a new float variable.
4. JPY Calculation: Calculate how many JPY the original Euro amount (from step 1) corresponds to. Store this result also in a new float variable.
5. Output: Display all results clearly and neatly formatted on the console. Show the original EUR amount, the converted USD amount, and the converted JPY amount.
6. Comments: Add meaningful comments to your code explaining what individual sections do and why certain variables were named as they were. Pay attention to sensible indentation of your code.
"""

amount  = float(input("Enter amount in Euros (EUR): "))  # Prompt user for Euro amount and store as float
eur_to_usd = 1.08  # Exchange rate from EUR to USD
eur_to_jpy = 165.25  # Exchange rate from EUR to JPY

usd_calculation = amount * eur_to_usd  # Calculate equivalent USD amount
jpy_calculation = amount * eur_to_jpy  # Calculate equivalent JPY amount

print(f"{amount:.2f} EUR is equivalent to {usd_calculation:.2f} USD.") # Display converted USD amount
print(f"{amount:.2f} EUR is equivalent to {jpy_calculation:.2f} JPY.") # Display converted JPY amount

# ***************************************************

# Task 2: The Intelligent Profile Analysis Tool

""" Requirements
1. Data Collection: Prompt the user consecutively to enter the following information:
- Name (String)
- Age (Integer)
- Hometown (String)
- Profession (String)
- The question: "Are you interested in Python programming? (yes/no)" (Expect 'yes' or 'no' and convert the answer into a Boolean variable).
2. Variables: Store each input in a suitably named variable with the correct data type.
3. Age Category: Based on the entered Age, assign a category to the user. Store this category as a String in a new variable:
- If the age is less than 25: "Young Enthusiast"
- If the age is 25 or greater: "Experienced Professional"
4. Profile Output: Create a comprehensive yet concise profile summary. This should contain all collected information as well as the derived age category and be attractively displayed on the console. Ensure that the output is easily readable and structured.
5. Comments: Use comments to explain the declaration of variables and especially the logic for the age category.
"""

name = input("\n\nEnter your name: ")  # Prompt user for their name
age = int(input("Enter your age: "))  # Prompt user for their age and convert
hometown = input("Enter your hometown: ")  # Prompt user for their hometown
profession = input("Enter your profession: ")  # Prompt user for their profession
print("Are you interested in Python programming? (yes/no): ")
answer = input()

if answer == 'yes':
    interested_in_python = True # Convert response to Boolean
else:
    interested_in_python = False  # Convert response to Boolean

if age < 25:
    age_category = "Young Enthusiast"  # Assign category for users under 25   
else:
    age_category = "Experienced Professional"  # Assign category for users 25 and older
    
# Display the comprehensive profile summary
print("\n--- User Profile Summary ---")
print(f"Name: {name}")
print(f"Age: {age} ({age_category})")
print(f"Hometown: {hometown}")
print(f"Profession: {profession}")
print(f"Interested in Python Programming: {'Yes' if interested_in_python else 'No'}")
print("----------------------------")

# ***************************************************





