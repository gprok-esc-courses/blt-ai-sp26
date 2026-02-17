
def factorial(n):
    if n == 0 or n == 1:    # Base Case
        return 1
    else: 
        return factorial(n - 1) * n
    

f = factorial(5)
print(f)