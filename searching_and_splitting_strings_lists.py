fname = input("Enter file name: ")
#fname = "mbox-short.txt"
fh = open(fname)
count = 0
#for loop to iterate through the file
for line in fh:
    if line.startswith('From '):
        final_form = line.split()
        count += 1
        print(final_form[1]) #this calls on the 2nd item in the list using 1 (0,1,2...)
        


print("There were", count, "lines in the file with From as the first word")
