'''
10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
Sample value of n is 5
Expected Result : 615
'''

a = int(input("Enter the value of n : "))

n1 = int(a)
n2 = int(f"{a}{a}")# string theke integer banay nilam.string value hye add hyese..tarpor integer banay neya hoyese evabe
n3 = int(f"{a}{a}{a}")

print(n1+n2+n3)