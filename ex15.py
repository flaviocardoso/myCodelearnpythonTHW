from sys import argv #import of system argv

script, filename = argv #argument of scropt and file name (insert)

txt = open(filename) # open file 

print ("Here's your file %r" % filename) # print a string describer the file name
print (txt.read()) # print from read file

print ("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print (txt_again.read())