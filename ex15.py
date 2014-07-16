from sys import argv

script, filename = argv
# opens a file (file is passed in as a parameter durin execution)
txt = open(filename)
#prints string plus 'filename'
print "Here's your file %r:" % filename
# prints the text from the text file that was passed in
print txt.read()
# prompts user to type filename to be read
print "Type the filename again:"
# creates variable where user input is store, gives a '>' as 
# cursos/prompt. User input is name of text file to be opened.
file_again = raw_input("> ")
# creates variable to store the text inside file
txt_again = open(file_again)
# prints/reads text from the variabl 'txt_again'
print txt_again.read()