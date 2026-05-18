#Anthia Gardner-Celestine
#Question 1
messy_menu = "    PizZA, burGER, SaLAd "
# a.) Using strip function to remove leading and trailing white space
clean_menu = messy_menu.strip()
print(clean_menu)

#b.) Changing string to lower case
lower_menu = clean_menu.lower()
print(lower_menu)

# c.) Display message that lists the menu
print("Today’s special menu list:" ,lower_menu)

#Question 2
# a.) Using the range() function to create a list of all even numbers from 2 to 50 (inclusive).
even_numbers = list(range(2, 51, 2))

# b.) Display numbers
print(even_numbers)

# c.) Calculate and print the total number of items in the list
total_number = len(even_numbers)
print(total_number)

# d.) Calculate and print the sum of all the numbers
total_sum = sum(even_numbers)
print(total_sum)

# e.)Using multiplier stored in a constant variable, calculating the product of the multiplier 
# with the sum of the maximum and minimum number in the list.
MULTIPLIER = 2
maximum_number = max(even_numbers)
minimum_number = min(even_numbers)
result = MULTIPLIER * (maximum_number + minimum_number)
print(result)

#Question 3
# a.) Guest list with four names
guest_list = ["paul", "mia", "jason", "jamie"]
print(guest_list)

# b.) Add ‘linus’ to the end of the list
guest_list.append("linus")
print(guest_list)

# c.) Add ‘guido’ to the beginning of the list
guest_list.insert(0, "guido")
print(guest_list)

# d.) Sort the list alphabetically and permanently
guest_list.sort()
print(guest_list)

# e.) Use a list comprehension to create a new list called invitations
#that contains the string "You are invited, <Name>!" for every guest in the list, 
#with their names capitalized.
invitations = [f"You are invited, {guest.capitalize()}!" for guest in guest_list]
print(invitations)

# f.)Use a slice to print only the first three invitations from your new list.
print(invitations[0:3])
