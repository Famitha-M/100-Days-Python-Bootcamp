programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}
print(programming_dictionary["Function"])

dict1={
    123:"hello",
    "hello":123
}
print(dict1[123])
print(dict1["hello"])

# Empty Dictionary
dict2={
}

# Wipe An Existing Dictionary
programming_dictionary={}
print(programming_dictionary)

# Adding dict value to existing dictionary
dict1["loop"]="this is a loop"
print(dict1)

# Edit an Item in a Dictionary
dict1[123]="Hi"
print(dict1)

# Loop through a dictionary
for i in dict1:
    print(i)
    print(dict1[i])
