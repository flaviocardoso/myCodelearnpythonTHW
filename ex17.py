# from system  import argv
from sys import argv
# from os.path import exists
from os.path import exists

# enter script, first file and second file on prompt
script, from_file, to_file = argv

# print string of assing files
print ("Copying from %s to %s" % (from_file, to_file))

# we could do these two on one line too, how?

# open file 'from_file' to assing 'in_file'
in_file = open(from_file)
# read file above of value 'indata' 
indata = in_file.read()

# print string with lenght to value of file
print ("The input file is %d bytes long" % len(indata))

# print string to show it exist the file
print ("Does the output file exist? %r" % exists(to_file))
# print defenitions to continue and contents about file
print("Ready, hit RETURN to continue, CTR-C to about.")
# input to return or about but not insert
input("> ")

# open file 'to_file' on definition  'w'(open to writting)
out_file = open(to_file, 'w')
# enter to write about definition
out_file.write(indata)

print ("Alright, all done.")

# here botton describ close files
out_file.close()
in_file.close()