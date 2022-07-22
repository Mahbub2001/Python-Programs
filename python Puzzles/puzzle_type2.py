'''
 We are making n stone piles! The first pile has n stones. If n is even, then all piles have an even number of stones. If n is odd, all piles have an odd number of stones. Each pile must more stones than the previous pile but as few as possible. 
 Write a Python program to find the number of stones in each pile. 
 '''

def testing(n):
    return [n + 2 * i for i in range(n)]

print(testing(2))
print(testing(17))
