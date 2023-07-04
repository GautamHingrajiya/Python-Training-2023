technology = input("Enter Technology : ")

# get first 3 character from string

print("First Three Character : ", technology[:3])

# get last three character from string

print("last Three Character : ", technology[-3:])

# get last character from string

print("Last Character : ", technology[-1])

# get middle string

print("Three to Five Character : ", technology[3:5])

# The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())

# The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())

# The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J")) # returns Jello, World! 

# The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = "apple"
price = 49.95
myorder = "I want {} pieces of item {} for {} rupees."
print(myorder.format(quantity, itemno, price))

# ordering by number passing in 
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
