# let the user know what's going on
print ("Welcome to Cat & Dog Cafe!")
print ("Answer the questions below to play.")
print ("-----------------------------------")

# Collect names and personalities
cat_name = input("What is the cat's name? ")
cat_personality = input("An adjective to describe the cat: ")
dog_name = input("What is the dog's name? ")
dog_personality = input("An adjective to describe the dog: ")

# Details about the cafe and its menu
shop_name = input("What is their cafe called? ")
location = input("Where is the cafe? ")
main_dish = input("What is their main dish? ")
dessert = input("What dessert do they serve? ")
drink = input("What drink do they serve? ")

# Details about the customers
your_name = input("What is your name? ")
guest_animal = input("What animal visits the cafe unexpectedly? ")

# Convert the answers into numbers
servings = int(input("How many servings do they prepare? "))
price = float(input("How much does one serving cost in dollars? "))

# Convert the answer into a boolean
is_spicy = input("Is the main dish spicy? Enter yes or no: ") == "yes"


# this is the story. it is made up of strings and variables.
# the \ at the end of each line let's the computer know our string is a long one
# (a whole paragraph!) and we want to continue more code on the next line. 
# play close attentiomimin to the syntax!

story = "One morning, " + cat_name + ", a " + cat_personality+ " cat, and " + dog_name + ", " + \
"a " + dog_personality + " dog, opened a cafe called " + shop_name + " in " + location + ". "\
+ cat_name + " cooked " + str(servings) + " servings of " + main_dish + \
", while " + dog_name + " prepared " + dessert + " and " + drink + ". "\
"Each serving of " + main_dish + " cost $" + str(price) + ". 
"On the menu, they wrote: the main dish Spicy level: " + str(is_spicy) + ".' "\
+ "Their first customer, " + your_name + ", ordered the whole menu! "\
"Just then, a " + guest_animal + " rushed into the cafe and stole the " + dessert + ". "\
+ dog_name + " chased the thief, while " + cat_name + " calmly poured another cup of " + drink + ". "\
"'Just another normal day at " + shop_name + ",' said " + cat_name + "."

# finally we print the story
print(story)
