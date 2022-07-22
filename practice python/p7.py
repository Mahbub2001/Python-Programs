'''
7. Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
'''

file_name = input("Enter the file name : ")

f_extension = file_name.split(".")

print(f"The extension of the file is : {f_extension[-1]}")


