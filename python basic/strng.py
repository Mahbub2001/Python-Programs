name = "Tony Stark"

# print(name.upper())
# print(name.lower())

# print(name.find('stark'))
# print(name.find('Stark'))

# ##reaplacing
# print(name.replace("Tony Stark","Ironman"))
# print(name.replace("Tony","Ironman"))
# print(name.replace("T","M"))
# print("m" in name) #subsring finding


# #######################################################


# ##concrating two strings
# greeting = "Good Morning,"
# name = "Turza"
# print(greeting + name)



##accessing
greeting = "Turza"
print(name[2])
print(name[-1])#reverse
print(name[:4])#minimum theke 4 prjnto like name[0:4]
print(name[1:])#eto theke maximum prjnto like name [1:5]
c = name[-4:-1] #same as [1:4]
print(c)



# ##slacing
# print(name[0:3])





##skip some carracter
name2 ="TurzaIsGood"
e = name2[1:4:2]#index 1 theke 4 prjnto jabe and proti ta por ekta digit skip krbe
print(e)
name1 = "TurzaIsGood"
d= name1[0 :: 3]#ekta print kre porer duitake skip korbe ..evabe chlte thakbe
print(d)
#ortthat 2 dile 1 3 dile 2 4 dile 3 evabe skip krbe



########################################################
####functions of strings

# story = "once upon a time there was a student named Turza who was very brilliant and talented"

# #string functions
# print(len(story))
# print(story.endswith("talented"))#verify the ending string true /false
# print(story.count("i"))##count carracters
# print(story.count("was"))##count words too
# print(story.capitalize())##capitalize the first word 
# print(story.find("a"))##index number (sudhu first occurence er)
# print(story.replace("Turza","Mahbub"))##sb occurence k replace korbe


####escape suquesce (\n,\t,\,\\)

# story = "Turza is good.\nHe is very good"
# print(story)