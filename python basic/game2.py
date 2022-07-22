'''
The game function in a program lets a user play a game returns the score as an integer. you need to read a file
'History.txt' which is either blank or contains the previous HIgh Score.You need to write a program to update the High Score 
whenever game() breaks the High Score
'''

# def game():
#     return 68

# score = game()

# with open("High_Score.txt","r") as f:
#     High_Score = int(f.read())

# if High_Score < score:
#     with open("High_Score.txt","w") as f:
#         f.write(str(score))#str typecast krte hbe nahle hbe na ..c file always str nay


def game():
    return 68


score = game()

with open("High_Score.txt", "r") as f:
    High_Score_str = f.read()

if High_Score_str == '': # eti alada vabe lekha lagle cz qs e lekha ase j jdi faka hoy taholeo write krte hbe
    with open("High_Score.txt", "w") as f:
        # str typecast krte hbe nahle hbe na ..c file always str nay
        f.write(str(score))


elif int(High_Score_str) < score:##interger e typecast krte hbe cz file e always string e thake
    with open("High_Score.txt", "w") as f:
        # str typecast krte hbe nahle hbe na ..c file always str nay
        f.write(str(score))
