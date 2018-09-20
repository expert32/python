print ("creating a text file with write () method" )
text_file = open("Abc.txt","w")

text_file.write("Line S\n")
text_file.write("Line 2\n")
text_file.write("Line 3\n")
text_file.close()
                
text_file = open("Abc.txt", "r")
print (text_file.read())
text_file.close()
