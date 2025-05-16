# Read a text file and print its contents

myFile = open("./my_text.txt", "r")
text = myFile.read()
myFile.close()
print(text)
