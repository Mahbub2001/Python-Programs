# marks = {"english" : 95,"chemistry" : 98}
# information = {"tonmay" : "fer"}

# print(marks["chemistry"])

# marks["physics"] = 97##adding value
# print(marks)

# marks["physics"] = 99 #changing data value
# print(marks)

# mydict = {
#     "Fast": "In a Quick Manner",
#     "Turza" : "A coder",
#     "Marks":[1,2,3],
#     "another":{'Harry':"Player"}#another dictionary like nested
# }

# print(mydict["Fast"])
# print(mydict["Marks"])
# print(mydict["another"]["Harry"])

# #changing value:
# mydict["Marks"] = [23,2,42]#mutable,changing possible
# print(mydict["Marks"])

###########################################Method#######################################

mydict = {
    "Fast": "In a Quick Manner",
    "Turza" : "A coder",
    "Marks":[1,2,3],
    "another":{'Harry':"Player"},
    1 : 2
}

print(mydict.keys()) # keys gulo print korar jnno use krte hy
print(type(mydict.keys()))
print(list(mydict.keys()))#type casting....list e banay nilam
print(mydict.values())##value gulo print krar jnno
print(mydict.items()) ##prints all value and contents of dictionary


#####update dictionary by adding key - values pair from updateDict
updateDict = {
    "Lovish" : " friend",
    "Ruman" : "Friend"
}
mydict.update(updateDict)
print(mydict)    


print(mydict.get("harry"))#nine dekhabe
# print(mydict["harry2"]) # error dekhabe
