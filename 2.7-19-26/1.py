#Sample String
text = "Welcome to IMCC"

#1. Strip spaces from both ends
print("Remove Spaces",text.strip())

#2. Convert to lowercase
print("Lower Case",text.lower())

#3. Convert to uppercase
print("Upper vase", text.upper())

#4. Capitalose first letter
text = text.strip()
print(text.title)

#5. Title case(Capitalise each word)
print(text.title)

#6. Count occurrences of a substring 
print("Letter C occurs",text.count("C"),"times in text")

#7. Find the position of a substring (-1 if not found)
print("Position of IMCC is",text.find)