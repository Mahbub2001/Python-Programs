'''
write a program to generate multiple tables from 2 to 20 and write it to the different files.Place these files fin a folder for a 13-years old
'''

for i in range(2, 21):
    with open(f"table/multiplication_table_of_{i}.txt", "w") as f:#table/multiplication_table_of_ lekhar karon holo table folder er vtore txt file ta banaor jnno
        for j in range(1,11):
            f.write(f"{i} X {j} = {i*j}")
            if j!=10:
                f.write('\n')



