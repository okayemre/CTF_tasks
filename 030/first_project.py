name_1 = input("Enter the first name: ")

print(f"\nHello, {name_1}!")

age = int(input("\nEnter your age: "))
weight = float(input("\nEnter your weight in kg: "))
wahr = True

print(f"\n{name_1} is {age} years old.")

print(f"\n{name_1} type: {type(name_1)}")
print(f"{age} type: {type(age)}")
print(f"{wahr} type: {type(wahr)}")
print(f"{weight} type: {type(weight)}")

if age > 18:
    print(f"\n{name_1} is older than 18.")
    wahr = False
elif age == 18:
    print(f"\n{name_1} is exactly 18 years old.")
    wahr = True
else:
    print(f"\n{name_1} is younger than 18.")
    wahr = False

print(f"\nYour age is {wahr}")
