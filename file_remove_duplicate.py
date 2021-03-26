fname = input("Enter file name: ")
fh = open(fname)

#create a string of the file we are opening
string = fh.read()

#now split it into a list
lst = string.split()

#create a blank list
final_list = []

#create a loop to check for unique words
for unique in lst:
    while unique not in final_list: #while unique is not in the new final_list
        final_list.append(unique) #add the unique word

#sort into alphabetical order
final_list.sort()
print(final_list)
