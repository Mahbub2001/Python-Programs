'''
write a program to find out the line number where python is present from pratice 13

'''
content = True
i = 1
with open("log.txt","r") as f:
    while content:
        content = f.readline()
     
        if "python" in content.lower():# sbgulo lower kre neya hoyese jate kre boro soto somossa na hoy khujte ...
             print(content)
             print(f"Yes python is present on line number {i}")
        i+=1
