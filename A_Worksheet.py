'''
#print(len (input ("What is your name? ")))
#name = input ("What is your name? ")
#length = len(name)
#print(length)
#print("123" + "456")
#num_char = len(input("What is your name?"))

#new_num_char = str(num_char)
#print("Your name has " + new_num_char + " characters.")

#a = str(123)
#print(type(a))

#two_digit_number = input("Type a two digit number: ")
#print(two_digit_number)
#first_digit = two_digit_number[0]
#second_digit = two_digit_number[1]
#print(first_digit)
#print(second_digit)
#result = int(first_digit) + int(second_digit)
#print(result)

states_of_america = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

#print(states_of_america[-3])
 
#states_of_america.extend(["aISH"])

print(len(states_of_america))

states_of_india = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka",
    "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram",
    "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana",
    "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"
]

indian_union_territories = [
    "Andaman and Nicobar Islands",
    "Chandigarh",
    "Dadra and Nagar Haveli and Daman and Diu",
    "Lakshadweep",
    "Delhi (National Capital Territory of Delhi)",
    "Puducherry",
    "Ladakh",
    "Jammu and Kashmir"
]

dirty_dozen =["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears","Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
#print(dirty_dozen)
#print(dirty_dozen[0])
#print(dirty_dozen[1])
#print(dirty_dozen[1][2])
#print(dirty_dozen[1][3])
print(dirty_dozen[1][1])


fruits = ["Apple","Banana", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")

# for Loop with range
for number in range(1,11,3):
    print(number)
    
total = 0
for number in range(1,101):
    total += number
print(total)

total1 = 0
for number in range(2,101,2):
    total1 += number
print(total1)

total2 = 0 
for number in range(1,101):
    if number % 2 == 0:
        total2 += number
print(total2)        
'''

for number in range(1,101):
    if (number % 3 == 0) and (number % 5 == 0):
        number = "fizzbuzz"
    elif number % 3 == 0:
        number = "fizz"
    elif number % 5 == 0:
        number = "buzz"
    else:
        print(number)


