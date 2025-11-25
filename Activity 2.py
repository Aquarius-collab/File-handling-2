new_file = open("Codingal.txt" , "x")
new_file.close()
import os
print("Checking if the file exists or not...")
if os.path.exists("Codingal.txt"):
    os.remove("Codingal.txt")
else:
    print("The file does not exist,")
my_file = open("my_file.txt" , "w")
my_file.write("Hi! I am Penguin. I am 1 yr old.")
my_file.close()
os.remove("Codingal.txt")