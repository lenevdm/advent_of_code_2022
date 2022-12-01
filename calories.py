# Find the elf with the most calories. How many calories are they carrying?

# Loop through the lines of the file.
# Find the spaces

# variable_name = variable_value


#open the file
file = open("calories.txt", "r")

#read the file into a list
data = file.read()
data_into_list = data.replace('\n', ",").split()

#print data
print(data_into_list)

#close the file like a good boy
file.close()

#loop through the list, adding up list items until there is a empty item -> ,,




# print("Sum of all elements in the list: ", total)